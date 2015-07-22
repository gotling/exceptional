class NoException(Exception):
    def __init__(self, message='Error: No Exception'):
        self.message = message
        print message


class StringException(Exception):
    def __init__(self, message=''):
        self.message = message
