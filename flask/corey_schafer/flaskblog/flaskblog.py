import config

from flask import Flask
from flask import flash, url_for, redirect, render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY

posts = [
    {
        'author': 'Rohit Rao',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Sep 7, 2021',
    },
    {
    'author': 'Rohit Doppelgänger',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Sep 8, 2021',
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'home.html',
        posts = posts,
    )

@app.route('/about')
def about():
    return render_template(
        'about.html',
        title='About'
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(
            f'Account created for {form.username.data}!',
            'success',
        )
        return redirect(url_for('home'))
    else: 
        return render_template(
            'register.html',
            title = 'Register',
            form = form,
        )

@app.route('/login')
def login():
    form = LoginForm(),
    return render_template(
        'login.htl',
        title = 'Login',
        form = form
    ),

if __name__ == '__main__':
    app.run(debug=True)
