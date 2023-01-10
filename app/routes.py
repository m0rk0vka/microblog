from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'morkovka'}
    posts = [
        {
            'author': {'username' : 'Morty'},
            'body' : 'Beautiful day in Russia!'
        },
        {
            'author': {'username' : 'Alexsander'},
            'body' : 'Today I stay home with Mary!'
        }
    ]
    return render_template('index.html', title='Home Page', user=user, posts=posts)
