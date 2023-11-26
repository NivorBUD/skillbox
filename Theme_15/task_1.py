import os


class File:
    def __init__(self, filename: str, mod: str):
        self.filename = filename
        self.mod = mod
        self.File = None

    def __enter__(self):
        if os.path.exists(self.filename):
            self.file = open(self.filename, self.mod, encoding='UTF-8')
        else:
            print('Такой файл не существует. Создан файл в режиме записи')
            self.file = open(self.filename, 'w', encoding='UTF-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True
