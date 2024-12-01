import os
from datetime import timedelta

class Config:
    # Base directory of the application
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    # Secret key for session management
    SECRET_KEY = 'your-secret-key-here'  # In production, use environment variable
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'flights.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Application configuration
    DEBUG = True  # Set to False in production
    TESTING = False
    
    # Session configuration
    PERMANENT_SESSION_LIFETIME = timedelta(days=31)
    
    # Flight tracking system specific settings
    FLIGHT_UPDATE_INTERVAL = 60  # seconds
    MAX_SEARCH_RESULTS = 100
    
    # Timezone settings
    TIMEZONE = 'UTC'
    
    # API Configuration (if needed for future expansion)
    API_VERSION = '1.0'
    API_PREFIX = '/api/v1'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    
    # In production, use environment variables for sensitive data
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    
    # Production database URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(Config.BASE_DIR, 'flights.db')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

# Get current configuration
def get_config():
    config_name = os.environ.get('FLASK_CONFIG') or 'default'
    return config[config_name]