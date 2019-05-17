from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'News Highlight'

    return render_template('index.html',txt = message)

@app.route('/news/<int:news_id>')
def movie(news_id):

    '''
    View news source function that returns the news sources
    '''
    return render_template('movie.html',id = news_id)