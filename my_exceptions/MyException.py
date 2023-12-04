
class MyException(Exception):
    """ An eaxmple of a custom exception that can be thrown """

    def __int__(self, message):
        super().__init__(message)
        self.message = message

