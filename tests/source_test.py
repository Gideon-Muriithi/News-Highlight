import unittest
from app.models import Source

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
