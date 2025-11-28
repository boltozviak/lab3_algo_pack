class FuncError(Exception):
    pass

class InvalidValueError(FuncError):
    def __init__(self, *args):
        super().__init__(*args)
