import  math

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


class SampleMiddlewareTwo(BaseMiddleware):

    def __init__(self):
        super().__init__()
        self.m = None

    def process(self, m):
        self.m = m
        s = 0
        for i in range(m['processed']+1):
            s += math.pi*m['processed']**0.5/math.log10(m['processed'])
        m['sqaredprocessed'] = s
        return m