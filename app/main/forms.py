from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError, BooleanField
from wtforms.validators import DataRequired,Email

class ReviewForm(FlaskForm):

     title = StringField('Review title',validators=[DataRequired()])

     review = TextAreaField('Movie review')

     submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

