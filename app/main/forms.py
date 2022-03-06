from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):

     title = StringField('Comment title',validators=[DataRequired()])

     comment = TextAreaField('Comment')

     submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('TWe would like to know you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
     title = StringField('Title',validators = [DataRequired()])
     category = SelectField('Category', choices= [('Email','Email'),('Business Idea','Business Idea'),('Social Media','Social Media')],validators=[DataRequired()])