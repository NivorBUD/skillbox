import random


class Student:
    def __init__(self, name, group_number=0):
        self.name = name
        self.group_number = group_number
        self.grades = [random.randint(2, 5) for _ in range(5)]
        self.avgGrade = sum(self.grades) / 5

    def print(self):
        print('Имя ученика: {}; Средний балл: {}'.format(self.name, self.avgGrade))