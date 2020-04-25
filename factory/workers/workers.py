from factory.workers.worker import MetaWorker


class FactoryWorker(metaclass=MetaWorker):
    def __init__(self):
        pass

    def run_worker(self):
        pass

    def connect_to_feed(self):
        '''
        in case of kakfa topics with multiple partitions use this method to increase speed
        should return iterable consumer
        '''
        return iter()

    def connect_to_queue(self):
        '''in general case read from engines feed queue'''

    def get_result(self):
        return

class ProcessingWorker(FactoryWorker):
    '''in case with kafka '''
    def __init__(self, settings):
        self.settings = settings
        pass
