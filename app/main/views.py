from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_sources,get_article,search_news


# Views
@main.route('/')
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

@main.route('/articles/<id>')
def articles(id):
    '''
    View articles for a single source
    '''
    all_articles = get_article(id)
    title = f'NewsApp -- {id}'
    id_articles = id

    return render_template('articles.html', articles=all_articles, title=title, id_id=id_articles)

@main.route('/search/<keywords>')
def source_search(keywords):
     searched_news = search_news(keywords)
     title = f'search results for {keywords}'
     return render_template('search.html',title=title,articles=searched_news)

