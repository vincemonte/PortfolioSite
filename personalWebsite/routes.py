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
    project_post = Project.query.get_or_404(project_id)
    files = get_project_files(project_post)
    return render_template('project.html', project_post=project_post, files=files)

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

def save_file(form_file, proj_dir_path):
    fn = secure_filename(form_file.filename)
    file_path = os.path.join(proj_dir_path, fn)
    form_file.save(file_path)
    return fn

def save_project_files(form):
    #create the relative path to make directory
    rel_dir_path = os.path.join(app.config['UPLOAD_FOLDER'], form.title.data.strip().replace(" ", ""))
    full_dir_path = os.path.join(app.root_path, 'static', rel_dir_path)
    os.mkdir(full_dir_path)
    for file in form.files.data:
        save_file(file, full_dir_path)
    return rel_dir_path

'''
Returns all files in the project's directory as a full file path
Return type: list
'''
def get_project_files(project):
    full_dir_path = os.path.join(app.root_path, 'static', project.files)
    files = os.listdir(full_dir_path)
    file_paths = []
    for file in files:
        # we simply join them here to avoid concatenation in HTML file
        file_paths.append(os.path.join(project.files, file))
    return file_paths

@app.route('/addpost', methods=['GET', 'POST'])
def addpost():
    form = PostForm()
    if form.validate_on_submit():
        project_post = Project(title=form.title.data, type=form.type.data, content=form.content.data)
        if form.files.data:
            # we assign the full path retuned from save_project_files function to the Project db object
            project_post.files = save_project_files(form)
        type_image = set_type_image(form.type.data)
        home_post = HomePost(type_image=type_image, content=form.synopsis.data, project=project_post)
        db.session.add(project_post)
        db.session.add(home_post)
        db.session.commit()
        flash('Post has been created.', 'success')
        return redirect(url_for('homepage'))
    return render_template('addpost.html', title="New Post",form=form)
