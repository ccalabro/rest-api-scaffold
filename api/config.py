class Config(object):
    """General Configuration class"""
    def __init__(self):
        pass

    @staticmethod
    def init_app(app):
        """Initialize app

        :type app: Flask object
        :param app: Flask application object. The application in itself.
        """
        pass

class DevelopmentConfig(Config):
    """Development Configuration class"""
    DEBUG = True

    def __init__(self):
        super(DevelopmentConfig, self).__init__()


class TestingConfig(Config):
    """Testing Configuration class.

    Intended to use to run tests.
    """
    TESTING = True
    DEBUG = True

    def __init__(self):
        super(TestingConfig, self).__init__()


class StagingConfig(Config):
    """Staging Configuration class

    Intended to use to test application in a pre-production environment
    """
    DEBUG = False

    def __init__(self):
        super(StagingConfig, self).__init__()


class ProductionConfig(Config):
    """Production Configuration class"""
    DEBUG = False

    def __init__(self):
        super(ProductionConfig, self).__init__()


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
