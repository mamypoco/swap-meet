from swap_meet.decor import Decor
from swap_meet.errors import InvalidIDError


def create_decor_class(id):
    """
    Tries to create a Decor object with the given ID.

    Handles:
        InvalidIDError: Prints the error message if the ID is not valid.
    """

    try:
        decor = Decor(id)
        
    except InvalidIDError as err:
        print(err)

create_decor_class("id")
