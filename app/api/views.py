from fastapi import APIRouter
from loguru import logger

from app.api.models import Mail
from app.celery.tasks import send_message_task

router = APIRouter()


@router.post('/mail')
def send_mail(mail: Mail):
    logger.debug(f'Receiver: {mail.receiver}')
    send_message_task.delay(mail.receiver)
    return mail
