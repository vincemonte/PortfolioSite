from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    type_image = SelectField('Project Type', validators=[DataRequired()],choices=[('code', 'Coding'), ('writing', 'Writing'), ('photography','Photography')])
    submit = SubmitField('Post')
