class News:
    '''
    News class to define a news objects
    '''
    def __init__(self,author,title,description,urlToImage,publishedAt,content):
    
        self.author=author
        self.title=title
        self.description=description
        self.urlToImage= urlToImage
        self.publishedAt=publishedAt
        self.content=content

class Sources:
    '''
    Source class to define sources
    '''
    def __init__(self,id,name,description,url,category,language,country):
        self.id=id
        self.name=name
        self.description=description
        self.url=url
        self.category=category
        self.language=language
        self.country=country

class Articles:
    '''
    article class to define an article
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
    
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt
        self.content=content

