import unittest
from app.models import NewsHighlight

class NewsHighlightTest(unittest.TestCase):

    '''
    Test Class to test the behaviour of the NewsHighlight class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_highlight = NewsHighlight('BCC', 'Come', 'I am a hero', 'url', 'Image', 'date','publishedAt')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_highlight, NewsHighlight))
