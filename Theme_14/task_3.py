from datetime import datetime
import functools
from typing import Callable


def logging(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func():
        print()
        print(func.__name__)
        print(func.__doc__)
        try:
            return func()
        except IndexError as e:
            with open('function_errors.log', 'a', encoding="utf-8") as errors_file:
                errors_file.write(str(datetime.now()) + str(type(e).__name__) + '\n')

    return wrapped_func


@logging
def test():
    """
    Тестовая исправная функция
    """
    print('<Тут что-то происходит...>')


@logging
def test_exception():
    """
    Тестовая функция с ошибкой
    """
    raise IndexError


test()
test_exception()
