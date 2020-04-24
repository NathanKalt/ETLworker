import asyncio
from aiomultiprocess import Worker
from .task import Task
from .settings import settings


async def run_worker(task_msg, config):
    task = Task(task_msg, config)
    await task.run()
    return task.get_fin_info()


class TaskManager:
    def __init__(self, engine, task, queue):
        self.engine = engine
        self.task_msg = task
        self.result_queue = queue

    async def run(self):
        w = Worker(target=run_worker, args=(self.task_msg, self.engine.settings))
        r = await w
        await self.result_queue.put({'task_mngr': self, 'result': r})

    def __eq__(self, other):
        return self.task_msg.get('task_id') == other.task_msg.get('task_id')

class Engine:
    def __init__(self):
        self.settings = settings


    async def run(self):
        await self.connector.start()
        asyncio.ensure_future(self.listen_results())
        await self.listen_tasks()

    async def listen_tasks(self):
        async for msg in self.connector.engine_consumer:

            task_msg = msg.value
            await self.task_queue.put(1)
            logger.info('task received with task_id "{}"'.format(jp.search('task_id', task_msg)))
            task_mngr = TaskManager(
                self,
                task_msg,
                self.result_queue,
            )
            asyncio.ensure_future(task_mngr.run())
            self.running_tasks.append(task_mngr)

    async def listen_results(self):
        while True:
            result = await self.result_queue.get()
            self.running_tasks.remove(result.get('task_mngr'))
            await self.task_queue.get()
            await self.connector.send_to_topics(result.get('result'))
            # print(result.keys())
            logger.info('task finished')