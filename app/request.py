from app import app
import urllib.request,json
from .models import news

News = news.News
Sources = news.Sources

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
N_base_url = app.config['NEWS_API_BASE_URL']
S_base_url = app.config['SOURCE_API_BASE_URL']

def get_news(source):
    '''
    Function to get the json response to our url request
    '''
    get_news_url = N_base_url.format(source,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
    print(news_results)
    return news_results

def process_results(news_list):
    '''
    Function to process movie results obtained by the api to 
    convert it to a list of objects
    
    Args:
        news_list: list of dictionaries with news details
    Returns:
        news_results: list of news objects
    '''

    news_results = []
    for news_item in news_list:
    
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        publishedAt= news_item.get('publishedAt')
        content = news_item.get('content')
        
        print(news_item)

        if urlToImage:
            news_object = News(author,title,description,urlToImage,publishedAt,content)
            news_results.append(news_object)
            print(news_object)

    return news_results

def get_sources(category):
    get_sources_url = S_base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)

    return sources_results


def process_sources(sources_list):
    '''
    A function  that processes the sources result and transform them to a list of Objects
    Args:
        sources_list; A list of dictionaries that contain catnews details
t:
    Returns :
        sources_results; A list of sources objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')

        print(sources_item)

        if id:
            sources_object =Sources(id,name,description,url,category,language,country)
            sources_results.append(sources_object)

    return sources_results
