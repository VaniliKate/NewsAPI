class Config:

    '''
        General configuration parent class
    '''

    API_KEY = "ac4fe71ff54045d781683a87a8bbad28"

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


        