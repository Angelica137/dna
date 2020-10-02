import os
import logging.config
from distutils.util import strtobool


HOST = '0.0.0.0'
PORT = 8080
STATIC_ROOT = 'app/static'

try:
    DEBUG = strtobool(os.environ.get('DEBUG'))
except (ValueError, AttributeError):
    DEBUG = False

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
SEND_FILE_MAX_AGE_DEFAULT = 0

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(name)s %(levelname)s %(message)s',
            'dateformat': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'default': {
            'level': LOG_LEVEL,
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': LOG_LEVEL,
            'propagate': True
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
