import functools
from typing import Callable


def decorator_with_args_for_any_decorator(decorator_func: Callable) -> Callable:
    def decorator(*args, **kwargs):
        def wrapped_func(func: Callable) -> Callable:
            return decorator_func(func, *args, **kwargs)
        return wrapped_func
    return decorator


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*func_args, **func_kwargs) -> Callable:
        print("Переданные арги и кварги в декоратор:", args, kwargs)
        return func(*func_args, **func_kwargs)

    return wrapped_func


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
