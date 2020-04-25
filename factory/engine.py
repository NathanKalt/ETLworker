from factory.workers.workers import ProcessingWorker
from factory.utils.utils import object_from_settings
import factory.settings as settings
from importlib import import_module
from aiomultiprocess import Worker
import asyncio



async def run_worker(task_msg, settings):
    worker = ProcessingWorker(task_msg, settings)
    await worker.run()
    return worker.get_result()


class Engine:
    '''main process run the whole service from here'''
    def __init__(self, settings, connector):
        self.settings = settings
        self.feed = object_from_settings(settings.FEED_PIPELINE)
        self.stream = object_from_settings(settings.STREAM_PIPELINE)
        self.feed_queue = asyncio.Queue()
        self.stream_queue = asyncio.Queue()
        self.running_tasks = []

    async def create_workers(self):
        pass

    async def run(self):
        await self.feed.start()
        asyncio.ensure_future(self.listen_results())
        await self.listen_tasks()

    async def listen_results(self):
        while True:
            result = await self.stream_queue.get()
            self.running_tasks.remove(result.get('task_mngr'))
            await self.stream_queue.get()
            await self.stream_queue.send_to_topics(result.get('result'))

