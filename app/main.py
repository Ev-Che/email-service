from fastapi import FastAPI
from loguru import logger

from app.api.kafka_consumer import Consumer

app = FastAPI()

logger.debug('Starting listening')
Consumer().listen()
