from celery import Celery
from loguru import logger

from app.config import BROKER_CONN_URI, BACKEND_CONN_URI

logger.debug(BROKER_CONN_URI)
logger.debug(BACKEND_CONN_URI)

celery = Celery(__name__)
logger.debug('Celery app starts')
celery.conf.broker_url = BROKER_CONN_URI
celery.conf.result_backend = BACKEND_CONN_URI

celery.autodiscover_tasks()
