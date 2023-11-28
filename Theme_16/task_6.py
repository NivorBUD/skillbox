import functools
import time
from typing import Callable


class ClassDecorator:
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs) -> Callable:
        print("Вызов функции", self.func.__name__)
        print("Аргументы:", str(args) + ",", kwargs)
        start_time = time.time()
        result = self.func(*args, **kwargs)
        run_time = time.time() - start_time
        print("Результат:", result)
        print("Время выполнения:", run_time)
        return result


@ClassDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется “сложный” алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    # Можете попробовать вынести создание файла из циклов и проверить, сколько времени алгоритм будет работать в этом случае
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)
