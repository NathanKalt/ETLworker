from importlib import import_module
import re


def object_from_settings(path):
    modstring = path
    comp = re.split('\.', modstring)
    module = '.'.join(comp[0:-1])
    name = comp[-1]
    m = import_module(module)
    return getattr(m, name)() #weird =)