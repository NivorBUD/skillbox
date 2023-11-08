from functools import reduce
from typing import List, Counter

print("Задание 1")
floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

floats_2 = list(map(lambda x: round(x ** 3, 3), floats))
names_2 = list(filter(lambda x: len(x) >= 5, names))
numbers_2 = reduce(lambda prev_num, cur_num: prev_num * cur_num, numbers)

print(floats_2)
print(names_2)
print(numbers_2)

print("\nЗадание 2")
letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(map(lambda x, y: (x, y), letters, numbers))
print(result)

print("\nЗадание 3")
def can_be_poly(text: str) -> bool:
    return len(list(filter(lambda count: count % 2, Counter(text).values()))) <= 1


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))

print("\nЗадание 4")
def count_unique_characters(text: str) -> int:
    return len(list(filter(lambda x: x in text.lower(), 'qwertyuiopasdfghjklzxcvbnm')))


message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
