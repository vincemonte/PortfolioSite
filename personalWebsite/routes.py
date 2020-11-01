import os
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from PIL import Image
from personalWebsite import app, db, bcrypt
from personalWebsite.forms import PostForm, LoginForm
from personalWebsite.models import User, Project, HomePost
from personalWebsite.utils import save_file, save_project_files, get_project_files, set_type_image, get_first_files, is_safe_url, delete_project_files

@app.route('/')
@app.route('/home')
def homepage():
    page = request.args.get('page', 1, type=int)
    posts = HomePost.query.order_by(HomePost.id.desc()).paginate(page=page, per_page=6)
    return render_template('homepage.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')

#Eventually each project will need its own type of route
@app.route('/project/<title>')
def project(title):
    project_post = Project.query.filter_by(title=title).first()
    #still assigning files as so and potentially returning None makes this easier on the Jinga templating
    files = get_project_files(project_post)
    return render_template('project.html', project_post=project_post, files=files)

@app.route('/coding')
def coding():
    page = request.args.get('page', 1, type=int)
    posts = Project.query.filter_by(type='coding').order_by(Project.id.desc()).paginate(page=page, per_page=10)
    return render_template('coding.html', posts=posts)

@app.route('/writings')
def writings():
    page = request.args.get('page', 1, type=int)
    posts = Project.query.filter_by(type='writing').order_by(Project.id.desc()).paginate(page=page, per_page=10)
    return render_template('writings.html', posts=posts)

@app.route('/photography')
def photography():
    page = request.args.get('page', 1, type=int)
    posts = Project.query.filter_by(type='photography').order_by(Project.id.desc())
    files = get_first_files(posts)
    posts=posts.paginate(page=page, per_page=10)
    return render_template('photography.html', posts=posts, files=files)



@app.route('/addpost', methods=['GET', 'POST'])
@login_required
def addpost():
    if current_user.is_authenticated:
        form = PostForm()
        if form.validate_on_submit():
            project_post = Project(title=form.title.data, type=form.type.data, content=form.content.data, author=current_user)
            #interesting note: the request processes there to be data in the multiple file field and therefore it isn't as simple as checking the
            # data from request; rather, we can check if there is no filename associated with the MultipleFileField
            upload = request.files['files']
            if upload.filename != '':

                project_post.files = save_project_files(form)
            type_image = set_type_image(form.type.data)
            home_post = HomePost(type_image=type_image, content=form.synopsis.data, project=project_post)
            db.session.add(project_post)
            db.session.add(home_post)
            db.session.commit()
            flash('Post has been created.', 'success')
            return redirect(url_for('homepage'))
        return render_template('addpost.html', title="New Post",form=form)
    else:
        return redirect(url_for('homepage'))

@app.route('/post/<int:proj_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(proj_id):
    project_post = Project.query.get_or_404(proj_id)
    home_post = HomePost.query.filter_by(project_id=proj_id).first()
    if project_post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        project_post.title = form.title.data
        project_post.type = form.type.data
        project_post.content = form.content.data
        upload = request.files['files']
        if upload.filename != '':
            delete_project_files(project_post)
            project_post.files = save_project_files(form)
        if request.form.get('del-images'):
            delete_project_files(project_post)
            project_post.files = None
        home_post.type_image = set_type_image(form.type.data)
        home_post.content = form.synopsis.data
        db.session.commit()
        flash('Your post has been updated.', 'success')
        return redirect(url_for('project', title=project_post.title))
    elif request.method == 'GET':
        form.title.data = project_post.title #filling in the form with the current data
        form.synopsis.data = home_post.content
        form.type.data = project_post.type
        form.content.data = project_post.content
    return render_template('addpost.html', title="Update Post", form=form, legend='Update Post', update=True)

@app.route('/post/<int:proj_id>/delete', methods=['POST'])
@login_required
def delete_post(proj_id):
    project_post = Project.query.get_or_404(proj_id)
    home_post = HomePost.query.filter_by(project_id=proj_id).first()
    if project_post.author != current_user:
        abort(403)
    delete_project_files(project_post)
    db.session.delete(project_post)
    db.session.delete(home_post)
    db.session.commit()
    flash('Your post has been deleted', 'success')
    return redirect(url_for('homepage'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('homepage')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            if not is_safe_url(next_page):
                return flask.abort(400)
            return redirect(next_page) if next_page else redirect(url_for('homepage'))
        else:
            flash('Login unsuccessful. Check your password, Vince', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))
