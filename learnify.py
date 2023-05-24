from flask import Flask, render_template, url_for, flash, redirect, request
from forms import LearnForm, RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '8019c12b3dc1d9f77267997bec460e1d'

global_variable = None

def question_bank (input):
    import openai
    API_KEY = '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'
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
    API_KEY = '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'
    openai.api_key = API_KEY
    model_id = 'gpt-3.5-turbo'
    n = '10'
    sentence = 'Give me ' + n + ' resources on ' + input
    conversation = []
    conversation.append({'role' : 'system', 'content' : sentence})
    response = openai.ChatCompletion.create(
      model = model_id,
      messages = conversation
    )
    output = response['choices'][0]['message']['content'].split('\n')
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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You Have Been Logged In!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please Check Username And Password', 'danger')
    return render_template('login.html', title='Log In', form=form)

if __name__ == '__main__':
    app.run(debug=True)
