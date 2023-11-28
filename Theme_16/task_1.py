import functools
from typing import Callable


def check_permission(user_category: str) -> Callable:
    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapped_func():
            if user_category == "admin":
                return func()
            else:
                print("PermissionError: у пользователя недостаточно прав, чтобы выполнить функцию", func.__name__)

        return wrapped_func

    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
