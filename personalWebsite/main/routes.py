from flask import render_template, request, Blueprint
from personalWebsite import db, bcrypt
from personalWebsite.models import HomePost


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = HomePost.query.order_by(HomePost.id.desc()).paginate(page=page, per_page=6)
    return render_template('index.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html')
