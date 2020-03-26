from flask import render_template, url_for, flash, redirect, request
from personalWebsite import app

#Will be moved to their own python file
posts = [
    {
        'title': 'Polar Plotting Project',
        'content': 'This is what I did for my polar plotting project',
        'date_posted': 'March 22, 2020'
    },
    {
        'title': 'Documentation Streaming',
        'content': 'I streamlined Google form answers into MS Word documents like so',
        'date_posted': 'February 12, 2020'
    },
    {
        'title': 'Plague Writing',
        'content': "I recently wrote my thoughts on the current pandemic we're in",
        'date_posted': 'March 10, 2020'
    },
    {
        'title': 'Cooking Recipes',
        'content': "I took up a lot of cooking, being stuck at home and all.",
        'date_posted': 'March 20, 2020'
    }
]



@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html', posts=posts)

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/writings')
def writings():
    return render_template('writings.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/addpost')
def addpost():
    return render_template('addpost.html')
