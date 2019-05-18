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

class Source:
    '''
    Source class to define sources
    '''
    def __init__(self,id,name,description,url):
        self.id=id
        self.name=name
        self.description=description
        self.url=url    
