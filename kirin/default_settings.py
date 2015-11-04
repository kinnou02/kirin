#URI for postgresql
# postgresql://<user>:<password>@<host>:<port>/<dbname>
#http://docs.sqlalchemy.org/en/rel_0_9/dialects/postgresql.html#psycopg2
SQLALCHEMY_DATABASE_URI = 'postgresql://navitia:navitia@localhost/kirin'

NAVITIA_URL = 'https://api.navitia.io/'

NAVITIA_INSTANCE = 'sncf'

NAVITIA_TOKEN = None

CONTRIBUTOR = 'realtime.ire'


DEBUG = True

#rabbitmq connections string: http://kombu.readthedocs.org/en/latest/userguide/connections.html#urls
RABBITMQ_CONNECTION_STRING = 'pyamqp://guest:guest@localhost:5672//?heartbeat=60'

#queue used for task of type load_realtime, all instances of kirin must use the same queue
#to be able to load balance tasks between them
LOAD_REALTIME_QUEUE = 'kirin_load_realtime'

#amqp exhange used for sending disruptions
EXCHANGE = 'navitia'

ENABLE_RABBITMQ = True

#Log Level available
# - DEBUG
# - INFO
# - WARN
# - ERROR

# logger configuration
LOGGER = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] [%(levelname)5s] [%(process)5s] [%(name)25s] %(message)s',
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
        'amqp': {
            'level': 'DEBUG',
        },
        'sqlalchemy.engine': {
            'handlers': ['default'],
            'level': 'WARN',
            'propagate': False
        },
        'sqlalchemy.pool': {
            'handlers': ['default'],
            'level': 'WARN',
            'propagate': False
        },
        'sqlalchemy.dialects.postgresql': {
            'handlers': ['default'],
            'level': 'WARN',
            'propagate': False
        },
        'werkzeug': {
            'handlers': ['default'],
            'level': 'WARN',
            'propagate': False
        },
    }
}
