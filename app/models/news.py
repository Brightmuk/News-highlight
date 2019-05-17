class News:
    '''
    News class to define a news objects
    '''
    def __init__(self,id,name,author,title,urlToImage,description):
        self.id=id
        self.name=name
        self.author=author
        self.title=title
        self.urlToImage='https://image.tmdb.org/t/p/w500/' + urlToImage
        self.description=description
