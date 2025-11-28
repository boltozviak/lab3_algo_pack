class SortingError(Exception):
    pass

class TypeSortingError(SortingError):
    def __init__(self, *args):
        super().__init__(*args)
