from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, MultipleFileField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Optional


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    synopsis = TextAreaField('Synopsis', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[Optional()])
    #possibly add other file extension types
    files= MultipleFileField('Files', validators=[FileAllowed(['jpg', 'png'])])
    type = SelectField('Project Type', validators=[DataRequired()],choices=[('update', 'Update'), ('coding', 'Coding'), ('writing', 'Writing'), ('photography','Photography')])
    submit = SubmitField('Post')
