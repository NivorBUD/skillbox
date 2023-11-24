import functools
import time
from typing import Callable, Any


def slow_down(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func():
        time.sleep(2)
        return func()

    return wrapped_func


@slow_down
def test():
    print('<Тут что-то происходит...>')


test()
