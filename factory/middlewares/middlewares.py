
class BaseMiddleware:

    def __init__(self, m=None):
        self.m = m


    def process(self, m):
        return m


class SampleMiddleware(BaseMiddleware):

    def __init__(self):
        super().__init__()
        self.m = None

    def process(self, m):
        self.m = m
        m['processed'] = m['data']*m['data']
        return m


class SampleMiddleware_two(BaseMiddleware):

    def __init__(self):
        super().__init__()
        self.m = None

    def process(self, m):
        self.m = m
        m['sqaredprocessed'] = m['processed']**2
        return m