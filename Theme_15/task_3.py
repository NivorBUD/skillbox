from typing import List


class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string: str):
        if cls.is_date_valid(date_string):
            day, month, year = cls.get_data(date_string)
            return cls(day, month, year)

    @classmethod
    def get_data(cls, date_string: str) -> List:
        return list(map(int, date_string.split('-')))

    @classmethod
    def is_date_valid(cls, date_string: str) -> bool:
        data = cls.get_data(date_string)
        if len(data) != 3:
            return False
        day, month, year = data
        return 1 <= day <= 31 and 1 <= month <= 12 and year > 0

    def __str__(self):
        return "День:{}   Месяц:{}   Год:{}".format(self.day, self.month, self.year)


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
