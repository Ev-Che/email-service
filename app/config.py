import os

from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')

BROKER_CONN_URI = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
BACKEND_CONN_URI = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
