from flask import render_template
from app import app
from .request import get_news,get_sources,get_article


# Views
@app.route('/')
def index():

     '''
     View root page function that returns the index page and its data
     '''
     # Getting top headlines
     top_headlines = get_news('Top') 
     print(top_headlines)

     general = get_sources('general')
     title = 'News Highlights'
     return render_template('index.html', txt = title, top_headlines = top_headlines, general=general )

@app.route('/articles/<id>')
def article(id):

     '''
     View news source function that returns the news sources
     '''
     
     all_articles = get_article(id)
     
     print(all_articles)
     return render_template('articles.html', articles = all_articles, art=articles )



