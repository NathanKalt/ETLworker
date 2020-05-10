from importlib import import_module
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

    # print(methods_chain)
    return mw_chain