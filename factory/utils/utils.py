from importlib import import_module
import logging
import re

def prepare_module(path):
    modstring = path
    comp = re.split('\.', modstring)
    module = '.'.join(comp[0:-1])
    name = comp[-1]
    return import_module(module), name


def object_from_settings(path, *args):
    m, name = prepare_module(path)
    return getattr(m, name)(*args)

def get_middleware_chain(settings):
    mw_chain = []
    for path in settings.MIDDLEWARES:
        m, name = prepare_module(path)
        mw_chain.append(getattr(m, name)())
    return mw_chain

def get_app_logger(settings=None):
    logger = logging.getLogger('AioETL')
    logger.setLevel(logging.INFO)
    logging.getLogger("aiokafka").setLevel(logging.ERROR)
    level = logging.INFO

    if settings.LOG_LEVEL == 'DEBUG':
        level = logging.DEBUG

    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=level,
        datefmt='%Y-%m-%d %H:%M:%S')

    return logger