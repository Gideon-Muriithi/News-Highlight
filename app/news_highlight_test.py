import unittest
from models import news_highlight

NewsHighlight = news_highlight.NewsHighlight

class NewsHighlightTest(unittest.TestCase):

    '''
    Test Class to test the behaviour of the NewsHighlight class
    '''

    def setUp(self):
            '''
            Set up method that will run before every Test
            '''
            self.new_highlight = NewsHighlight('BCC', 'Come', 'I am a hero', 'url', 'Image', 'date')

    def test_instance(self):
            self.assertTrue(isinstance(self.new_highlight, NewsHighlight))


if __name__ == '__main__':
    unittest.main()