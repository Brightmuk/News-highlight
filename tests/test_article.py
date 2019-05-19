import unittest
from app.models import Articles
class ArticleTest(unittest.TestCase):

    def test_article(self):
        '''
        test_source checks that new news source objects are created
        '''
        self.new_article = Articles('me','bbc-news','Jesus','is alive','eng','kenya','no','who')
        self.assertTrue(isinstance(self.new_article,Articles))
