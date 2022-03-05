from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError, BooleanField
from wtforms.validators import DataRequired,Email

class CommentForm(FlaskForm):

     title = StringField('Comment title',validators=[DataRequired()])

     comment = TextAreaField('Pitch comment')

     submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

