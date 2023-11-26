from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.__cache = OrderedDict()
        self.__capacity = capacity

    def get(self, key):
        value = self.__cache.pop(key)
        self.__cache[key] = value
        return value

    def print_cache(self):
        print(self.__class__.__name__)
        for key, value in self.__cache.items():
            print(f"{key} : {value}")

    @property
    def cache(self):
        if self.__cache:
            key, value = list(self.__cache.items())[0]
            return f"{key} : {value}"
        else:
            return "cache is empty"

    @cache.setter
    def cache(self, new_element):
        if new_element[0] in self.__cache:
            del self.__cache[new_element[0]]
        elif len(self.__cache) == self.__capacity:
            self.__cache.popitem(last=False)
        self.__cache[new_element[0]] = new_element[1]


# Создаём экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)
# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3
# Получаем значение по ключу
print(cache.get("key2"))  # value2
# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")
# Выводим обновлённый кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
