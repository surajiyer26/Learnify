from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

def learnify (input):
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

app.config['SECRET_KEY'] = 'c5fa2045bd85d123cc54cf06c7baa045'

# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template('home.html', posts=posts)

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

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input = request.form['input']
        if input == 'competitive programming':
            return render_template('home.html', posts=posts)
        else:
            return render_template('home.html', posts=learnify(input))
    return '''
        <body>

        <link rel="stylesheet" href="homepage.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

        <div class="homepage">
        <div><button class="logo">Learnify!</button></div>
            <form method="post">

              <input type="text" id="input" name="input" placeholder = "What do you want to learn today?">
              <input type="submit" value="Learn" id="learn" >

             <div class="loading">
             <div class="loading-circle"></div>
             </div>

            </form>
            </div>

            </body>

            <style>

            .loading {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: transparent;
            z-index: 9999;
            }

            .loading-circle {
            margin-left:auto;
            margin-right:200px;
            margin-top: 10%;
            border: 10px solid #f3f3f3;
            border-top: 10px solid #3498db;
            border-radius: 50%;
            width: 80px;
            height: 80px;
            animation: spin 2s linear infinite;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            }

            @keyframes spin {
            0% {
                transform: rotate(0deg);
            }
            100% {
                transform: rotate(360deg);
            }
            }

            body {
            min-height: 100vh;
            background-color:#181818;
            margin: 0 auto;
            }

            .homepage{
            text-align:center;
            margin-top:100px;
             }

            form{
                text-align:center;
                margin-top:10px;
                font-size: 20px;
                position: relative;
                padding:10px;
                }

            #input{
            display: inline-block;
            border-radius: 20px;
            border: 1px solid;
            width: 700px;
            padding: 10px;
            margin-left: auto;
            margin-right: auto;
            font-size: 20px;
            margin-top: 10px;
            background-color:#f7fbfc;
            }

            #learn{
            background-color: #68c1f5;
            border: none;
            border-radius: 20px;
            font-size: 20px;
            padding: 8px;
            z-index:2;
            }
            #learn:hover{
            color:#ffffff;}

           .logo{
            margin-left:auto;
            margin-right:auto;
            text-decoration: none;
            color:#68c1f5;
            font-weight: 300;
            font-family: 'Courier New', Courier, monospace;
            font-weight: 900;
            background-color:#01165b;
            border-radius: 10px;
            padding: 10px;
            font-size: 85px;
            margin-top: 100px;
            border:none;

            width: 13ch;
            border-right: 5px solid #68c1f5;
            margin: 2rem auto;
            white-space: nowrap;
            overflow: hidden;

            animation: typing 2s steps(13, end), blink-caret 0.5s step-end infinite alternate;
            text-shadow: 2px 3px 3px hsl(209, 100%, 50%);

            }
            @-webkit-keyframes typing {
                from {
                    width: 0;
                }
            }
            @-webkit-keyframes blink-caret {
                50% {
                    border-color: transparent;
                }
            }

            .logo:hover{
            background-color:#68c1f5;
            color: #01165b;
            transform: scale(1.02)
            text-shadow: none;

            }

             </style>

             <script>
            const form = document.querySelector('form');
            form.addEventListener('submit', (event) => {
            event.preventDefault(); // prevent form from submitting
            const loading = document.querySelector('.loading');
            loading.style.display = 'block';
            setTimeout(() => {
                // Submit form after 2 seconds
                form.submit();
            }, 2000);
            });
            </script>
    '''

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')

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
