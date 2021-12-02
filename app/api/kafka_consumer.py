import json
import os

from kafka import KafkaConsumer
from loguru import logger

from app.celery import send_message_task


class Consumer:
    # TOPIC = 'success_trade'
    TOPIC = 'test'

    def __init__(self):
        self._consumer = KafkaConsumer(
            self.TOPIC,
            bootstrap_servers=os.environ.get('LOCAL_ADDRESS'),
            auto_offset_reset='earliest',
            value_deserializer=self._deserializer
        )

    @staticmethod
    def _deserializer(message):
        return json.loads(message.decode('utf-8'))

    def listen(self):
        for message in self._consumer:
            logger.debug(f'Got Message: {message.value}')
            send_message_task(message.value)
            logger.debug('All messages sent')
