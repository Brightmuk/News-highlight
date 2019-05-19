import unittest
from app.models import Sources

class SourceTest(unittest.TestCase):

    def test_source(self):
        '''
        test_source checks that new news source objects are created
        '''
        self.new_source = Sources(1,'bbc-news','Jesus','is alive','eng','who','kenya')
        self.assertTrue(isinstance(self.new_source,Sources))
