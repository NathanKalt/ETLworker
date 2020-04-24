from importlib import import_module
import asyncio
from factory.pipelines.feedpipelines import KafkaFeedPipeline
from factory.pipelines.streampipelines import KafkaStreamPipeline
from factory import settings


async def run():
    # feed = KafkaFeedPipeline('logs')
    stream = KafkaStreamPipeline()
    try:
        for i in await stream.generate_whatever().__anext__():

            print(i)
    finally:
        pass
    # await stream.stream(stream.generate_whatever())

    # await feed.generate_whatever()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())