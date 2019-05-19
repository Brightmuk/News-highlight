import unittest
from app.models import News



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





