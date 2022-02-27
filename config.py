import os

class Config:
    
    NEWS_API_BASE_URL = 'https://newsapi.org/v2'
    NEWS_API_KEY = '5ee6e7e121684b06b9d0f6b8a2fb7671'
    SECRET_KEY = '4121'
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey={}'.format(NEWS_API_KEY)
    NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}