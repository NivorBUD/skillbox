import os.path


def gen_files_path(path: str = os.path.join('..')) -> list[str]:
    res = list()
    for root, dirs, files in os.walk(path):
        res.extend([os.path.join(root, file) for file in files])
    return res


user_path = input('Путь до каталога: ')
print(gen_files_path(user_path))
print(gen_files_path())
