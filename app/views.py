from flask import render_template
from app import app
from .request import get_news


# Views
@app.route('/')
def index():

     '''
     View root page function that returns the index page and its data
     '''
     # Getting top headlines
     top_headlines = get_news('sports') 
     print(top_headlines)
     title = 'News Highlights'
     return render_template('index.html', txt = title, top_headlines = top_headlines )

@app.route('/news/<int:news_id>')
def movie(news_id):

     '''
     View news source function that returns the news sources
     '''
     return render_template('movie.html',id = news_id)

