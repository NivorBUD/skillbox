import functools
from typing import Callable
from datetime import datetime
import time


def log_methods(date: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            launch_date = (date.replace("d", str(datetime.now().day))
                           .replace("Y", str(datetime.now().year))
                           .replace("H", str(datetime.now().hour))
                           .replace("M", str(datetime.now().minute))
                           .replace("S", str(datetime.now().second))
                           .replace("b", str(datetime.now().month)))
            print("Запускается '{}'. Дата и время запуска: {}".format(func.__name__, launch_date))
            start_time = time.time()
            result = func(*args, **kwargs)
            run_time = round(time.time() - start_time, 3)
            print("Завершение {}, время работы = {}".format(func.__name__, run_time))
            return result

        return wrapped_func

    @functools.wraps(decorator)
    def decorate(cls):
        for method_name in dir(cls):
            if not method_name.startswith("__"):
                cur_method = getattr(cls, method_name)
                decorate_method = decorator(cur_method)
                setattr(cls, method_name, decorate_method)
        return cls

    return decorate


@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
