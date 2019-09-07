class Config:
    '''
    General configuration parent class
    '''
   	NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
   	ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'

clMOVIE_API_BASE_URLass ProdConfig:
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig:     
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True   