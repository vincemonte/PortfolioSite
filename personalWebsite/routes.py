import os
from flask import render_template, url_for, flash, redirect, request
from PIL import Image
from personalWebsite import app, db
from personalWebsite.forms import PostForm
from personalWebsite.models import Project, HomePost
from werkzeug.utils import secure_filename

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
@app.route('/project/<int:project_id>')
def project(project_id):
    post = Project.query.get_or_404(project_id)
    files = os.listdir(post.files)
    return render_template('project.html', post=post, files=files)

@app.route('/coding', methods=['GET'])
def coding():
    posts = Project.query.filter_by(type='coding')
    return render_template('coding.html', posts=posts)

@app.route('/writings')
def writings():
    posts = Project.query.filter_by(type='writing')
    return render_template('writings.html', posts=posts)

@app.route('/photography')
def photography():
    posts = Project.query.filter_by(type='photography')
    return render_template('photography.html', posts=posts)


def set_type_image(form_type_image):
    path = 'images/'
    if form_type_image == 'code':
        fname = 'coding_project_type.png'
    elif form_type_image == 'writing':
        fname = 'writing_project_type.png'
    else:
        fname = 'photography_project_type.png'
    path += fname
    return path

def save_file(form_file, dir_title):
    fn = secure_filename(form_file.filename)
    path = os.path.join(app.root_path, 'static/images/project_images', dir_title, fn)
    form_file.save(path)
    return fn

@app.route('/addpost', methods=['GET', 'POST'])
def addpost():
    form = PostForm()
    if form.validate_on_submit():
        project_post = Project(title=form.title.data, type=form.type.data, content=form.content.data)
        if form.files.data:
            file_dir_path = os.path.join(app.root_path, 'static/images/project_images', form.title.data).strip().replace(" ", "")
            os.mkdir(file_dir_path)
            for file in form.files.data:
                save_file(file, file_dir_path)
            project_post.files = file_dir_path
        type_image = set_type_image(form.type.data)
        home_post = HomePost(type_image=type_image, content=form.synopsis.data, project=project_post)
        db.session.add(project_post)
        db.session.add(home_post)
        db.session.commit()
        flash('Post has been created.', 'success')
        return redirect(url_for('homepage'))
    return render_template('addpost.html', title="New Post",form=form)
