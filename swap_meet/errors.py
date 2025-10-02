
class InvalidIDError(Exception):
    """Raised when the given ID is not a valid integer."""
    def __init__(self, id_value, msg="ID must be an integer"):
        self.id_value = id_value
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return self.msg
