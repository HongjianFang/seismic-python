class ArgumentError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class InitializationError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
