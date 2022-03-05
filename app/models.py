from flask_login import UserMixin
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    photos = db.relationship('PhotoProfile',backref = 'user',lazy = "dynamic")
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")
    pass_secure = db.Column(db.String(255))
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
class Pitch(db.Model):

    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    pitch = db.Column(db.String(400))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    likes = db.relationship('Likes', backref = 'likes', lazy = 'dynamic')
    dislikes = db.relationship('Dislikes', backref = 'dislikes', lazy = 'dynamic')
    
    def __repr__(self):
        return '<User %r>' % self.pitch