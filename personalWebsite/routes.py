from flask import render_template, url_for, flash, redirect, request
from personalWebsite import app, db
from personalWebsite.forms import PostForm
from personalWebsite.models import Post


@app.route('/')
@app.route('/home')
def homepage():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=6)
    return render_template('homepage.html', posts=posts)

@app.route('/coding')
def coding():
    return render_template('coding.html')

@app.route('/writings')
def writings():
    return render_template('writings.html')

@app.route('/photography')
def photography():
    return render_template('photography.html')

@app.route('/about')
def about():
    return render_template('about.html')

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

@app.route('/addpost', methods=['GET', 'POST'])
def addpost():
    form = PostForm()
    if form.validate_on_submit():
        type_image = set_type_image(form.type_image.data)
        post = Post(title=form.title.data, type_image=type_image, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash('Post has been created.', 'success')
        return redirect(url_for('homepage'))
    return render_template('addpost.html', title="New Post",form=form)
