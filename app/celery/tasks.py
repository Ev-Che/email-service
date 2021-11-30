from loguru import logger

from app.api.services import MailSender
from app.celery.worker import celery


@celery.task
def send_message_task(receiver):
    logger.debug('stark task send_message')
    MailSender().send_trade_success_mail(receiver)
    logger.debug('finish task send_message')
