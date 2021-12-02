import os
import smtplib
import ssl
from abc import ABC, abstractmethod
from email.message import EmailMessage

from loguru import logger


class AbstractMailSender(ABC):
    TRADE_SUCCESS_TOPIC = 'Success Trade'
    SUCCESS_MESSAGE = ('You have new Trade in the TradePlatform system. '
                       'Check it.')

    def __init__(self):
        self.smtp_server = os.environ.get('SMTP_SERVER')
        self.port = int(os.environ.get('PORT'))
        self.sender = os.environ.get('SENDER_MAIL')
        self.password = os.environ.get('SENDER_PASSWORD')
        self.context = ssl.create_default_context()

    @abstractmethod
    def send_mail(self, message: EmailMessage):
        pass


class MailSender(AbstractMailSender):

    def send_mail(self, message):
        with smtplib.SMTP_SSL(self.smtp_server, self.port,
                              context=self.context) as server:
            logger.debug('Server started')
            server.login(self.sender, self.password)
            logger.debug('logged in')
            server.send_message(message)
            logger.debug('message sent')

    def send_trade_success_mails(self, receivers: list):
        for receiver_mail in receivers:
            message = self._create_message(
                sender=self.sender, receiver=receiver_mail,
                topic=self.TRADE_SUCCESS_TOPIC,
                body=self.SUCCESS_MESSAGE)
            try:
                self.send_mail(message=message)
            except Exception:
                continue

    @staticmethod
    def _create_message(sender: str, receiver: str, topic: str,
                        body: str):
        message = EmailMessage()
        message['Subject'] = topic
        message['From'] = sender
        message['To'] = receiver
        message.set_content(body)

        return message
