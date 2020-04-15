from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Optional


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    synopsis = TextAreaField('Synopsis', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[Optional()])
    images = TextAreaField('Images', validators=[Optional()])
    type = SelectField('Project Type', validators=[DataRequired()],choices=[('coding', 'Coding'), ('writing', 'Writing'), ('photography','Photography')])
    submit = SubmitField('Post')
