
class WorkerManager:
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


class MetaWorker:
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        return x






