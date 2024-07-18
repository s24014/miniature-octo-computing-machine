help(sleep_for_a_while)

from functools import wraps
def show_begin_end(func):
    @wraps(func)
    def deco_func(*args, **kwargs):
        print('== start')
        result == func(
