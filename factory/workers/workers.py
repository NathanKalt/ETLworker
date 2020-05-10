from factory.utils.utils import get_middleware_chain


class FactoryWorker():
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

    def stop(self):
        return

class SampleWorker(FactoryWorker):
    '''in case with kafka '''
    def __init__(self, feed, stream, settings):
        self.settings = settings
        self.feed_queue = feed
        self.stream_queue = stream
        self.mw_chain = get_middleware_chain(self.settings)
        print(self.mw_chain)

    async def process(self, m):
        for mw_method in self.mw_chain:
            m = mw_method.process(m)

        return m

    async def start(self):
        print('started')
        while True:
            m = await self.feed_queue.get()
            if m is None: break
            m = await self.process(m)
            await self.stream_queue.put(m)
            print('processed', m)

