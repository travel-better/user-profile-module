import os

class Config:
    '''
    Parent config class that holds all inheritable configurations
    '''
    pass

class ProdConfig(Config):
    '''
    Production config class that hold production configurations
    '''
    pass

class TestConfig(Config):
    '''
    Testing config class holding testing configurations
    '''
    pass

class DevConfig(Config):
    '''
    Development config class that holds all development configurations
    '''
    DEBUG=True

config_options = {
'development': DevConfig,
'testing': TestConfig,
'production': ProdConfig
}
