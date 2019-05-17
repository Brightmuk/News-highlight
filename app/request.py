from app import app
import urllib.request,json
from .models import news

News = news.News
# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config['NEWS_API_BASE_URL']

def get_news(source):
    '''
    Function to get the json response to our url request
    '''
    get_news_url = base_url.format(source,api_key)

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