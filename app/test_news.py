import unittest
from models import news

News = news.News
Sources = news.Sources

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('Python Must Be Crazy','https://image.tmdb.org/t/p/w500/khsjha27hbs','me','you','christine','beautiful')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

class SourceTest(unittest.TestCase):

    def test_source(self):
        '''
        test_source checks that new news source objects are created
        '''
        self.new_source = Sources(1,'bbc-news','Jesus','is alive','eng','kenya')
        self.assertTrue(isinstance(self.new_source,Sources))




if __name__ == '__main__':
    unittest.main()