import os
from collections.abc import Iterable

print('Задача 3. Количество строк\n')


def get_lines_count(path: str = os.path.abspath(os.path.join('..'))) -> Iterable[int]:
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as py_file:
                    valid_lines = list(filter(lambda line: not line.startswith('#') and line.rstrip() != '', py_file))
                    yield len(valid_lines)


for lines_cnt in get_lines_count():
    print(lines_cnt)
