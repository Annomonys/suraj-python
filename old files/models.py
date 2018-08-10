# from flask_sqlalchemy import SQLAlchemy
# from werkzeug import generate_password_hash, check_password_hash
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# from datetime import datetime

# db = SQLAlchemy()

# class User(db.Model):
#     __tablename__ = 'users'
#     uid = db.Column(db.Integer, primary_key = True)
#     firstname = db.Column(db.String(100))
#     lastname = db.Column(db.String(100))
#     email = db.Column(db.String(100), unique=True)
#     pwhash = db.Column(db.String(200))

#     def __init__(self, firstname, lastname, email, password):
#         self.firstname = firstname.title()
#         self.lastname = lastname.title()
#         self.email = email.lower()
#         self.set_password(password)

#     def set_password(self, password):
#         self.pwhash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.pwhash, password)

# class Reset(db.Model):
#     __tablename__ = 'reset'
#     uid = db.Column(db.Integer, primary_key = True)
#     email = db.Column(db.String(100), unique = True)
#     resetcode = db.Column(db.String(20), unique = True)

#     def __init__(self, email, resetcode):
#         self.email = email.lower()
#         self.resetcode = resetcode.title()
    
#     def get_reset_token(self, expires_sec=3600):
#         s= Serializer(app.config['SECRET_KEY'], expires_sec)
#         return s.dumps({'user_id': self.id}).decode('utf-8')

#     @staticmethod
#     def verify_reset_token(token):
#         s = Serializer(pp.config['SECRET_KEY'])
#         try:
#             user_id = s.loads(token)['user_id']
#         except:
#             return None
#         return User.query.get(user_id)

from datetime import datetime
from __main__ import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    image_file = db.Column(db.String(100), nullable = False, default ='default.jpg')
    password = db.Column(db.String(100), nullable = False)
    posts =  db.relationship('Post', backref = 'author', lazy = True)

    def __repr__(self):
        return f"User('{self.fullname}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.data_posted}')"
