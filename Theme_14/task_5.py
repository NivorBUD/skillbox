import functools
from typing import Dict, Any, Callable


def hashed(func: Callable) -> Callable:
    hash_dict: Dict[Any, Any] = dict()

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        key = ("{}{}{}".format(func.__name__, args, kwargs))
        if key not in hash_dict:
            hash_dict[key] = func(*args, **kwargs)
        return hash_dict[key]

    return wrapped_func


@hashed
def fibonacci(num: int) -> int:
    if num <= 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(20))
print(fibonacci(30))
print(fibonacci(50))
print(fibonacci(60))
print(fibonacci(100))
