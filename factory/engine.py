from factory.workers.workers import ProcessingWorker
from factory.utils.utils import object_from_settings
from aiomultiprocess import Worker
import asyncio



async def run_worker(feed_queue, stream_queue):
    worker = ProcessingWorker(feed_queue, stream_queue)
    await worker.run()
    return worker.stop()


class Engine:
    '''main process run the whole service from here'''
    def __init__(self, settings, connector):
        self.settings = settings
        self.feed = object_from_settings(settings.FEED_PIPELINE)
        self.stream = object_from_settings(settings.STREAM_PIPELINE)
        self.feed_queue = asyncio.Queue(maxsize=settings.FEED_QUEUE_MAX_SIZE)
        self.stream_queue = asyncio.Queue()
        self.running_tasks = []


    async def run(self):
        for i in range(self.settings.AMOUNT_OF_WORKERS):
            w = Worker(target=run_worker,
                       args=(self.feed_queue, self.stream_queue, self.settings))

        await self.feed.start(self.settings.FEED_TOPIC, self.feed_queue)
        await self.stream.start(self.settings.STREAM_TOPIC, self.stream_queue)

        asyncio.ensure_future(self.listen_results())
        await self.listen_results()

    async def listen_results(self):
        while True:
            result = await self.stream_queue.get()
            self.running_tasks.remove(result.get('task_mngr'))
            await self.stream_queue.get()
            await self.stream_queue.send_to_topics(result.get('result'))

