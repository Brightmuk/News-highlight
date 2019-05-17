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
        
