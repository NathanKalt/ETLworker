from factory.pipelines.pipeline import MetaPipeline
from factory.connectors.connectors import KafkaConnector
from factory import settings
import asyncio
import random

class FeedPipeline(metaclass=MetaPipeline):
    '''feed pipeline is for middleware chain feed
    incoming data to factory comes from here
    fuel to the engine
    always has the start method to run proper connector and receive data
    '''
    def __init__(self):
        pass

    async def start(self):
        pass

    async def stop(self):
        pass


class KafkaFeedPipeline(FeedPipeline):

    def __init__(self, topic=None, queue=None):
        super().__init__()
        self.pipeline = KafkaConnector(topic)
        self.feed_queue = queue

    async def start(self):
        await self.pipeline.start_consumer()
        try:
            # Consume messages
            async for msg in self.pipeline.consumer:
                print("consumed: ", msg.topic, msg.partition, msg.offset,
                      msg.key, msg.value, msg.timestamp)
        finally:
            # Will leave consumer group; perform autocommit if enabled.
            await self.pipeline.consumer.stop()

    async def stop(self):
        await self.pipeline.consumer.stop()

