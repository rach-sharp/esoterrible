import builtins

reversed_builtin = reversed


def rotate_the_board(caller_globals):
    """Attempts to write reversed variables to the globals state the caller passes"""
    for v in caller_globals.copy():
        try:
            if isinstance(caller_globals[v], str):
                reversed_value = ''.join(reversed_builtin(locals()[v]))
            else:
                var_class = caller_globals[v].__class__
                reversed_value = var_class(reversed_builtin(caller_globals[v]))
            setattr(builtins, ''.join(reversed_builtin(v)), reversed_value)
        except Exception:
            pass


class DidNotRotateBoardException(Exception):
    pass


# Replace reversed with a lambda that throws an exception using dark magic - turns out it causes a lot of
# trouble though.
# noinspection PyTypeChecker
# builtins.reversed = lambda obj: (_ for _ in ()).throw(DidNotRotateBoardException('reversed is cheating!'))
