from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = '8019c12b3dc1d9f77267997bec460e1d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

global_variable = None

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken, please choose a different one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is taken, please choose a different one')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

def question_bank (input):
    import openai
    API_KEY = 'YOUR_API_KEY'
    openai.api_key = API_KEY
    model_id = 'gpt-3.5-turbo'
    n = '10'
    sentence = 'Frame ' + n + ' questions and their answers on ' + input
    conversation = []
    conversation.append({'role' : 'system', 'content' : sentence})
    response = openai.ChatCompletion.create(
        model = model_id,
        messages = conversation
    )
    x = response['choices'][0]['message']['content'].split('\n\n')
    output = []
    for i in range(0,int(n)):
        qna = x[i].split('\n')
        temp = {}
        temp['question'] = qna[0]
        temp['answer'] = qna[1]
        output.append(temp)
    return(output)

def resource (input):
    import openai
    API_KEY = 'YOUR_API_KEY'
    openai.api_key = API_KEY
    model_id = 'gpt-3.5-turbo'
    n = '10'
    sentence = 'Give me ' + n + ' resources on ' + input + ' and give a summary of each'
    conversation = []
    conversation.append({'role' : 'system', 'content' : sentence})
    response = openai.ChatCompletion.create(
      model = model_id,
      messages = conversation
    )
    output = response['choices'][0]['message']['content'].split('\n\n')
    return(output)

def library ():
    import openai
    API_KEY = 'YOUR_API_KEY'
    openai.api_key = API_KEY
    model_id = 'gpt-3.5-turbo'
    n = '10'
    sentence = 'list ' + n + ' libraries in mumbai'
    conversation = []
    conversation.append({'role' : 'system', 'content' : sentence})
    response = openai.ChatCompletion.create(
      model = model_id,
      messages = conversation
    )
    output = response['choices'][0]['message']['content'].split('\n\n')
    return(output)

app.config['SECRET_KEY'] = 'c5fa2045bd85d123cc54cf06c7baa045'

posts = [
    {
    'question': 'What is competitive programming?',
    'answer': 'Competitive programming is a type of programming competition where participants compete to solve algorithmic problems in a limited amount of time.'
    },
    {
    'question': 'How can one prepare for competitive programming?',
    'answer': ' One can prepare for competitive programming by practicing algorithmic problems, learning new data structures and algorithms, participating in online contests, and reviewing past solutions.'
    },
    {
    'question':'What are some common data structures used in competitive programming?',
    'answer':'Some common data structures used in competitive programming are arrays, linked lists, stacks, queues, heaps, trees, and graphs.'
    },
    {
    'question':'How can one optimize their solutions in competitive programming?',
    'answer':'One can optimize their solutions in competitive programming by using efficient algorithms, selecting appropriate data structures, minimizing unnecessary calculations, and avoiding redundant code.'
    },
    {
    'question':'How can one manage time effectively during a competitive programming contest?',
    'answer':'One can manage time effectively during a competitive programming contest by reading the problem statement carefully, understanding the constraints, prioritizing problems based on their difficulty, and staying calm under pressure.'
    }
]

@app.route("/")
def front():
    return render_template('front.html')

@app.route("/home", methods=['POST', 'GET'])
def home():
    input = request.form.get('input')
    global global_variable
    global_variable = input
    if input == 'competitive programming':
        return render_template('home.html', posts=posts)
    return render_template('home.html', posts=question_bank(input))

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')

@app.route("/resources")
def resources():
    return render_template('resources.html', title="Resources", posts=resource(global_variable))

@app.route("/libraries")
def libraries():
    return render_template('library.html', title='Library', posts=library())

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('front'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next') # to redirect the page you were tyrong to access, but couldnt because you werent logged in
            return redirect(next_page) if next_page else redirect(url_for('front'))
        else:
            flash('Login unsuccessful, please check email and password', 'danger')
    return render_template('login.html', title='Log In', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('front'))

if __name__ == '__main__':
    app.run(debug=True)
