from typing import Callable
import functools


def counter(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func():
        wrapped_func.count += 1
        print("Функция {} вызвана {} раз".format(func.__name__, wrapped_func.count))
        return func()

    wrapped_func.count = 0
    return wrapped_func


@counter
def test():
    print('<Тут что-то происходит...>')


test()
test()
test()
test()
