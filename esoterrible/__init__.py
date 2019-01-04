import builtins
import datetime
import time

from . import butterfinger_booleans, code_language_detection, looks_optimised_to_me, oxford_dictionary, esrever
from .esrever import rotate_the_board


def mischief_managed():
    """Undo most of what esoterrible changed in the session"""
    builtins.dict = oxford_dictionary.dict_builtin
    builtins.reversed = esrever.reversed_builtin
    time.sleep = looks_optimised_to_me.time_sleep
    datetime.datetime = code_language_detection.datetime_datetime
    for name in butterfinger_booleans.bool_truthiness:
        del name
