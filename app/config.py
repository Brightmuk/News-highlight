class Config:
    '''
    configuration parent class
    '''
    NEWS_API_BASE_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'
    SOURCE_API_BASE_URL='https://newsapi.org/v2/sources?category={}&language=en&apiKey={}'
    ARTICLE_API_BASE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'

    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True