from factory.utils.utils import object_from_settings, get_app_logger
import factory.settings as settings
import asyncio
from asyncio import Queue
import asyncpool
import logging


class Engine:
    '''main process run the whole service from here'''
    def __init__(self, settings):
        logger =get_app_logger(settings=settings)
        self.settings = settings
        self.feed = object_from_settings(settings.FEED_PIPELINE)
        self.stream = object_from_settings(settings.STREAM_PIPELINE)
        self.feed_queue = Queue(maxsize=settings.FEED_QUEUE_MAX_SIZE)
        self.stream_queue = Queue()
        self.worker_instance = object_from_settings(settings.WORKER_TYPE, self.feed_queue, self.stream_queue, self.settings)

    async def run(self):
        asyncio.ensure_future(self.feed.start(self.settings.FEED_TOPIC, self.feed_queue))
        asyncio.ensure_future(self.stream.start(self.settings.STREAM_TOPIC, self.stream_queue))
        async with asyncpool.AsyncPool(loop, num_workers=self.settings.AMOUNT_OF_WORKERS,
                                       name="workers_pool",
                                       logger=logging.getLogger("AioETL"),
                                       worker_co=await object_from_settings(settings.WORKER_TYPE,
                                                                            self.feed_queue,
                                                                            self.stream_queue,
                                                                            self.settings).start(),
                                       max_task_time=300,
                                       # log_every_n=10
                                       ) as pool:
            for i in self.feed_queue:
                await pool.push(i, self.stream_queue)


async def run_engine():
    e = Engine(settings)
    await e.run()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_engine())