import asyncio
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from factory import settings
import json

class MetaConnector(type):
    def __new__(cls, name, bases, dct):
        c = super().__new__(cls, name, bases, dct)
        return c


class BaseConnector(metaclass=MetaConnector):
    '''should always return 2 connectors producer and consumer
    - connections with dbs
    - connections to files
    - connections to brokers
    - connections to RSS feeds
    - etc
    '''
    def __init__(self):
        self.consumer = None
        self.produces = None


class KafkaConnector(BaseConnector):
    '''obiously a connector for kafka'''

    def __init__(self, topic):
        super().__init__()
        self.consumer = AIOKafkaConsumer(
            topic,
            loop=asyncio.get_event_loop(),
            bootstrap_servers=settings.BOOTSTRAP_SERVERS,
            value_deserializer=lambda m: json.loads(m.decode('utf8')),
        )

        self.producer = AIOKafkaProducer(
            loop=asyncio.get_event_loop(),
            bootstrap_servers=settings.BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        )

    async def start_producer(self):
        await self.producer.start()

    async def start_consumer(self):
        await self.consumer.start()


