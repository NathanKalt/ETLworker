from factory.validators.validator import MetaValidator
from cerberus import Validator


class BaseValidator(metaclass=MetaValidator):

    def __init__(self):
        self.validator = Validator()
        pass