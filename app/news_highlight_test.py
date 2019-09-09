import unittest
from models import news_highlight

NewsHighlight = news_highlight.NewsHighlight
Source = news_highlight.Source

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


    

class Source(unittest.TestCase):

    '''
    Test Class to test the behaviour of the NewsHighlight class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('BCC', 'Come', 'I am a hero', 'url', 'Image', 'date')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))



if __name__ == '__main__':
    unittest.main()