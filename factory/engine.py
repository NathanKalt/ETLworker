from factory.utils.utils import object_from_settings
import factory.settings as settings
from factory.workers.workers import SampleWorker
from aiomultiprocess import Pool
from multiprocessing import Queue
import asyncio
from asyncio import Queue


# async def run_worker(feed_queue, stream_queue):
#     worker = SampleWorker(feed_queue, stream_queue)
#     asyncio.ensure_future(worker.run())
#     # return worker.stop()

class Engine:
    '''main process run the whole service from here'''
    def __init__(self, settings):
        self.settings = settings
        self.feed = object_from_settings(settings.FEED_PIPELINE)
        self.stream = object_from_settings(settings.STREAM_PIPELINE)
        self.feed_queue = Queue(maxsize=settings.FEED_QUEUE_MAX_SIZE)
        self.stream_queue = Queue()
        self.worker_instance = object_from_settings(settings.WORKER_TYPE, self.feed_queue, self.stream_queue, self.settings)

    async def run(self):
        await asyncio.gather(
            self.feed.start(self.settings.FEED_TOPIC, self.feed_queue),
            self.stream.start(self.settings.STREAM_TOPIC, self.stream_queue),
            self.worker_instance.start()
        )


async def run_engine():
    e = Engine(settings)
    await e.run()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_engine())