from factory.utils.utils import get_middleware_chain
import logging


logger = logging.getLogger('AioETL')


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

    async def process(self, m):
        for mw_method in self.mw_chain:
            m = mw_method.process(m)
            logger.info('{} processing result {}'.format(mw_method.__class__.__name__, m))
            # print(m)

        return m

    async def start(self):
        logger.info('Worker {} started'.format(self.__class__.__name__))
        while True:
            m = await self.feed_queue.get()
            if m is None: break
            m = await self.process(m)
            await self.stream_queue.put(m)
            # print('processed', m)
            # return m

