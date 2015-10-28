__author__ = 'cosmin'


class CommandError(Exception):
    def __init__(self, arg):
        self.msg = arg


class InvalidParameters(Exception):
    def __init__(self, arg):
        self.msg = arg