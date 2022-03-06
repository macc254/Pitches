from flask import render_template,redirect,url_for,abort
from . import main
from .forms import CommentForm,UpdateProfile
from ..models import User,Comment
from flask_login import login_required, current_user
from .. import db
import markdown2  

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
   
    title = 'Home - Welcome to Pitches site'

    
    return render_template('index.html', title = title)


@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    # pitches = get_pitches(id)
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data

        # Updated review instance
        new_comment = Comment(pitch_id=id,pitch_title=title,pitch_comment=comment,user=current_user)

        # save review method
        new_comment.save_comment()
        return redirect(url_for('.pitch',id = id ))

    title = f'{title} comment'
    return render_template('new_comment.html',title = title,comment_form=form)
    
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/comment/<int:id>')
def single_comment(id):
    comment = Comment.query.get(id)
    if comment is None:
        abort(404)
    format_comment = markdown2.markdown(comment.pitch_comment,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('comment.html',comment = comment, format_comment = format_comment)