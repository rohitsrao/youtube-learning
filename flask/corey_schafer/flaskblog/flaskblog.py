from flask import Flask
from flask import render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Rohit Rao',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Sep 7, 2021',
    },
    {
        'author': 'Kristina Yanushko',
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

if __name__ == '__main__':
    app.run(debug=True)
