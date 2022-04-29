class Config:

    '''
        General configuration parent class
    '''

    API_KEY = "ac4fe71ff54045d781683a87a8bbad28"
    NEWS_BASE_URL_SOURCES = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    NEWS_BASE_EVERYTHING_URL = 'https://newsapi.org/v2/everything?domains={}&apiKey={}'
    NEWS_BASE_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_BASE_SOURCE = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

class ProdConfig(Config):

    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    pass

class DevConfig(Config):

    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


        