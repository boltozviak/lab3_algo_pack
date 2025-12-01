class StructureException(Exception):
    pass

class EmptyStackError(StructureException):
    def __init__(self, *args) -> None:
        super().__init__(*args)

class EmptyQueueError(StructureException):
    def __init__(self, *args) -> None:
        super().__init__(*args)
