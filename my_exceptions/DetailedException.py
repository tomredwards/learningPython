
class DetailedException(Exception):
    """ An eaxmple of a custom exception with an error code """

    def __int__(self, message, error_code):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

