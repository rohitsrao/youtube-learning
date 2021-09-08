from flask import flash, url_for, redirect, render_template
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

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
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            username = form.username.data,
            email = form.email.data,
            password = hashed_pw,
        )
        db.session.add(user)
        db.session.commit()
        flash(
            f'Your account has been created! You are now able to log in!',
            'success',
        )
        return redirect(url_for('login'))
    else: 
        return render_template(
            'register.html',
            title = 'Register',
            form = form,
        )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template(
        'login.html',
        title = 'Login',
        form = form,
    )
