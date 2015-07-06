"""General Module API"""

from flask import Flask
from config import config
from instance.iconfig import iconfig

import os


def create_app(config_name):
    """
    Generate app based on Flask instance.

    :type config_name: string
    :param config_name: Config Type (i.e. development, testing, staging, production, default).

    :rtype: Object
    :return: Flask Object.
    """
    app = Flask(__name__)

    # Load generic configs
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Load specific and sensitive configs
    app.config.from_object(iconfig[config_name])

    # Save environment type
    app.config['ENVIRONMENT'] = config_name

    # Register Blueprint
    from api_0_0_1 import api as api_0_0_1_blueprint
    app.register_blueprint(api_0_0_1_blueprint, url_prefix='/0.0.1')

    return app


try:
    if os.environ['ENV']:
        environment = os.environ['ENV']
except KeyError, e:
    environment = 'development'

app = create_app(environment)


if __name__ == '__main__':
    app.run(host=app.config['SERVER_SETTINGS']['host'], port=app.config['SERVER_SETTINGS']['port'])
