from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shelfio_database_dev',
        'USER': 'shelfio_database',
        'PORT': 5432,
        'HOST': 'shelfio-dev-db.ccsb0tt82qfi.us-east-2.rds.amazonaws.com',
        'PASSWORD': os.environ['AWS_PASSWORD'],

    }
}