from flask_login import UserMixin
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    pitches = db.relationship('Pitch',backref = 'author',lazy = "dynamic")
    likes = db.relationship('Likes', backref = 'like', lazy = 'dynamic')
    dislikes = db.relationship('Dislikes', backref = 'dislike', lazy = 'dynamic')
    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f'User {self.username}'
    
class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer)
    pitch_title = db.Column(db.String)
    pitch_comment = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    
    def save_comment(self,):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments
    
    
    def __repr__(self):
        return f'Comment {self.pitch_comment}'
class Pitch(db.Model):

    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    pitch = db.Column(db.String(400))
    pitch_title = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    likes = db.relationship('Likes', backref = 'likes', lazy = 'dynamic')
    dislikes = db.relationship('Dislikes', backref = 'dislikes', lazy = 'dynamic')
    
    def __repr__(self):
        return f'Pitch {self.pitch}'
    
class Likes(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    upvote = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_likes(cls,id):
        upvotes = Likes.query.filter_by(pitch_id =id).all()
        return upvotes

# class Dislikes(db.Model):
#     id = db.Column(db.Integer,primary_key = True)
#     downvote = db.Column(db.Integer)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

#     def save(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def get_dislikes(cls,id):
#         downvotes = Dislikes.query.filter_by(pitch_id =id).all()
#         return downvotes