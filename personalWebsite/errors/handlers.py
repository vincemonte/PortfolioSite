from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def handle_error_404(error):
    return render_template('errors/404.html'), 404 #note how we've returned the html and status code

@errors.app_errorhandler(403)
def handle_error_403(error):
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(500)
def handle_error_500(error):
    return render_template('errors/404.html'), 500

@errors.app_errorhandler(400)
def handle_error_400(error):
    return render_template('errors/400.html'), 400
