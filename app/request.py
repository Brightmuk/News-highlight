
import urllib.request,json
from .models import News,Articles,Sources



# Getting api key
api_key = None 

N_base_url = None 
S_base_url = None 
A_base_url = None 
SCH_base_url = None 

def configure_request(app):
    global api_key,N_base_url,S_base_url,A_base_url,SCH_base_url
    api_key = app.config['NEWS_API_KEY']
    N_base_url = app.config['NEWS_API_BASE_URL']
    S_base_url = app.config['SOURCE_API_BASE_URL']
    A_base_url = app.config['ARTICLE_API_BASE_URL']
    SCH_base_url = app.config['SEARCH_URL']

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
        
        

        if urlToImage:
            news_object = News(author,title,description,urlToImage,publishedAt,content)
            news_results.append(news_object)
            

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
        sources_object =Sources(id,name,description,url,category,language,country)
        sources_results.append(sources_object)
            

    return sources_results

def get_article(id):
    get_article_details_url = A_base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:

        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)
        
        article_object = []

        if article_details_response['articles']:
            articles_results_list = article_details_response['articles']
            articles_results = process_articles(articles_results_list)
            


    return articles_results



def process_articles(articles_list):
    '''
    Function  that processes the article result and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain article details
    Returns :
        articles_results: A list of article objects
    '''
    articles_results = []
    for articles_item in articles_list:
        
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
        content = articles_item.get('content')
        
        article_object = Articles(author,title,description,url,urlToImage,publishedAt,content)
        articles_results.append(article_object)
        print(articles_item)#test if its fetching
    return articles_results

def search_news(keyword):
    url = SCH_base_url.format(keyword,api_key)

    with urllib.request.urlopen(SCH_base_url) as response:
        data = json.loads(response.read())

        articles = []

        if data['articles']:
            articles_list = data['articles']
            articles = process_articles(articles_list)

    return articles

