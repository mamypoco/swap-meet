from swap_meet.decor import Decor

def create_decor_class(id):
    """
    Tries to create a Decor object with the given ID.

    Handles:
        : Prints the error message if the ID is not valid.
    """

    decor = Decor(id)

create_decor_class("id")
