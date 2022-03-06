from flask import render_template,redirect,url_for,abort,request
from idna import valid_string_length
from . import main
from .forms import CommentForm,UpdateProfile,PitchForm
from ..models import User,Comment,Pitch,Like,Dislike
from flask_login import login_required, current_user
from .. import db
import markdown2  

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    pitch = Pitch.query.all()
    email = Pitch.query.filter_by(category = 'Email').all()
    business = Pitch.query.filter_by(category = 'Business Idea').all()
    social = Pitch.query.filter_by(category = 'Social Media').all()
    title = 'Home - Welcome to Pitches site'

    
    return render_template('index.html',pitch = pitch, email = email,business = business,social = social,title = title)

@main.route('/pitch',methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        pitch_comment = form.pitch.data
        category = form.category.data
        user_id = current_user
        new_pitch = Pitch(pitch_comment=pitch_comment,category=category,user_id=current_user._get_current_object().id,title = title)
        return redirect(url_for('main.index'))
    return render_template('new_pitch.html', pitch_form=form )


@main.route('/comment/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    comment = Comment.query.filter_by(pitch_id = pitch_id).all()

    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id

        # Updated commentinstance
        new_comment = Comment(pitch_id=pitch_id,title=title,comment=comment,user_id=user_id)
        # save comment method
        new_comment.save_comment()
        return redirect(url_for('.comment',pitch_id = pitch_id ))

    title = f'{title} comment'
    return render_template('comment.html',title = title,form=form,pitch=pitch,comment=comment)
    
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_id = current_user._get_current_object().id
    pitch = Pitch.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,pitch=pitch)

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

@main.route('/like/<int:id>',methods=['GET','POST'])
@login_required
def like(id):
    get_pitches = Like.get_likes(id)
    valid_string = f'{current_user.id}: {id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string + " " + to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            new_like = Like(user=current_user,pitch_id=id)
            new_like.save()
            return redirect(url_for('main.index',id=id))
    