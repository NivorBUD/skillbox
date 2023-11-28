import functools


def singleton(cls):
    @functools.wraps(cls)
    def wrapped_func(*args, **kwargs):
        if not wrapped_func.instance:
            wrapped_func.instance = cls(*args, **kwargs)
        return wrapped_func.instance

    wrapped_func.instance = None
    return wrapped_func


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
