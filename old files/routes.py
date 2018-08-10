# from flask import Flask, flash, render_template, session, redirect, url_for
# from models import db, User
# from forms import SignupForm, LoginForm, AddressForm, Reset
# from flask import request
# from flask_mail import Mail, Message
# import random

# # from flaskext.mysql import MySQL
# # # from dbconnect import connection
# # app = Flask(__name__)
# # mysql = MySQL()


# # # MySQL configurations
# # app.config['MYSQL_DATABASE_USER'] = 'root'
# # app.config['MYSQL_DATABASE_PASSWORD'] = ''
# # app.config['MYSQL_DATABASE_DB'] = 'testpython'
# # app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# # mysql.init_app(app)



# app= Flask(__name__)
# mail=Mail(app)

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'suraj@qodemedia.com'
# app.config['MAIL_PASSWORD'] = 'kali bakhari'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)



# # @app.route('/register/', methods=["GET","POST"])
# # def register_page():
# #     try:
# #         conn = mysql.connect()
# #         return("Successfully connected")
# #     except Exception as e:
# #         return(str(e))    



# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://suraj:123456789@localhost/postgres'
# db.init_app(app)

# app.secret_key ="development-key"


# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")

# @app.route("/signup", methods = ["GET", "POST"])
# def signup():
#     if 'email' in session:
#         return redirect(url_for('home'))

#     form = SignupForm()
#     if request.method == "POST":
#         if form.validate() == False:
#             return render_template("signup.html", form = form)
#             flash('False')

#         else:
#             newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
#             db.session.add(newuser)
#             db.session.commit()
#             flash('Your Account is successfully Created')
#             return render_template("login.html", form = form)

#             session['email'] = newuser.email
#             return redirect(url_for('home'))
            
#     elif request.method == "GET":
#         return render_template("signup.html", form = form)
#         flash('False GET')


# @app.route("/login", methods = ["GET", "POST"])
# def login():
#     if 'email' in session:
#         return redirect(url_for('home'))

#     form = LoginForm()
#     if request.method == "POST":
#         if form.validate() == False:
#             return render_template('login.html',form = form)
#         else:
#             email = form.email.data
#             password = form.password.data

#             user = User.query.filter_by(email= email).first()
#             if user is not None and user.check_password(password):
#                 session['email'] = form.email.data
#                 return redirect(url_for('home'))
#             else:
#                 return redirect(url_for('login'))
    
#     elif request.method == "GET":
#         return render_template('login.html', form = form)


# @app.route("/logout", methods = ["GET", "POST"])
# def logout():
#     session.pop('email', None)
#     return redirect(url_for('index'))

# @app.route("/forget")
# def forget():
#     form = Reset()
#     if request.method == "POST":
#         if form.validate() == False:
#             return render_template('forget.html',form = form)
#         else:
#             email = form.email.data
#             resetcode = print(random.randint(0,90000))

#             print('Hello')
#             # newreset = Reset(email, resetcode)
#             # db.add(newreset)
#             # db.commit()

#             # flash('Please check Your email')
#             # return render_template('login.html', form = form)


#     elif request.method == "GET":
#         return render_template("forget.html", form = form)
#         flash('False GET')

    

# @app.route("/contact")
# def contact():
#     msg = Message('Hello', sender = 'suraj@qodemedia.com', recipients = ['suraj@qodemedia.com'])
#     msg.body = "Hello Flask message sent from Flask-Mail"
#     mail.send(msg)
#     return "Sent"

# @app.route("/home")
# def home():
#     if 'email' not in session:
#         return redirect(url_for('login'))
    
#     form = AddressForm()

#     if request.method == 'POST':
#         if form.validate() == False:
#            return render_template('home.html', form = form)
#         else:
#             pass

#     elif request.method == 'GET':
#        return render_template("home.html", form = form)
        

#     return render_template("home.html")

# if __name__ == "__main__":
#     app.run(debug = True)
    
    


from flask import Flask, flash, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime
# from flask import request
# from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'development-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://suraj:123456789@localhost/postgres'
db = SQLAlchemy(app)

from models import User, Post

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     fullname = db.Column(db.String(100), nullable = False)
#     email = db.Column(db.String(100), unique = True, nullable = False)
#     image_file = db.Column(db.String(100), nullable = False, default ='default.jpg')
#     password = db.Column(db.String(100), nullable = False)
#     posts =  db.relationship('Post', backref = 'author', lazy = True)

#     def __repr__(self):
#         return f"User('{self.fullname}', '{self.email}', '{self.image_file}')"

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     title = db.Column(db.String(100), nullable = False)
#     date_posted = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)
#     content = db.Column(db.Text, nullable = False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

#     def __repr__(self):
#         return f"Post('{self.title}', '{self.data_posted}')"


posts = [
    {
        'author' : 'Suraj',
        'title'  : 'Blog 1',
        'content' : 'First post',
        'date_posted' : 'April 10, 2018'
    },
    {
        'author' : 'Ram',
        'title'  : 'Blog 2',
        'content' : 'Second post',
        'date_posted' : 'April 20, 2018'
    }

]

# Home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home-new.html', posts = posts)

# About Page
@app.route("/about")
def about():
    return render_template('about-new.html', title = 'About')


# Register Page

@app.route("/register", methods =['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash( f'Account created for {form.fullname.data}!', 'success' )
        return redirect(url_for('home'))
    return render_template('register-new.html', title = 'Register', form = form)



# Login Page

@app.route("/login", methods =['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'test@gmail.com' and form.password.data == '12345678nine':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check Email and Passowrd', 'danger')
    return render_template('login-new.html', title = 'Login', form= form)



if __name__ == '__main__':
    app.run(debug = True)