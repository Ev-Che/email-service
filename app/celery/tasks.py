from loguru import logger

from app.api.services import MailSender
from app.celery.worker import celery


@celery.task
def send_message_task(receivers: list):
    logger.debug('stark task send_message')
    MailSender().send_trade_success_mails(receivers=receivers)
    logger.debug('finish task send_message')
