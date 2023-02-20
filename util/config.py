
"""Flask configuration."""


class FlaskConfig:
    """Base config."""
    JSON_SORT_KEYS = False


# we are not using this config yet
class ProdConfig(FlaskConfig):
    ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(FlaskConfig):
    ENV = 'development'
    DEBUG = True
    TESTING = True
