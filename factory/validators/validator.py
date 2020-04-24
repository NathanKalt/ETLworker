
class MetaValidator(type):
    def __new__(cls, name, bases, dct):
        c = super().__new__(cls, name, bases, dct)
        return c