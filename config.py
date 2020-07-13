import os

class Config:
    '''
    Parent config class that holds all inheritable configurations
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production config class that hold production configurations
    '''
    DEBUG=False

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
    COUCHDB_SERVER=os.environ.get('COUCHB_SERVER')
    COUCHDB_DATABASE=os.environ.get('COUCHB_DATABASE')


config_options = {
'development': DevConfig,
'testing': TestConfig,
'production': ProdConfig
}
