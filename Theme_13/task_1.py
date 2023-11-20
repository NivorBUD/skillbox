class Squares:
    def __init__(self, num: int):
        self.n = num
        self.counter = 0

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < self.n:
            self.counter += 1
            return self.counter ** 2
        else:
            raise StopIteration


def squaresGenerator(n: int):
    cur_num = 1
    for _ in range(n):
        yield cur_num ** 2
        cur_num += 1


n = int(input("Введите N: "))
class_iterator = Squares(n)
for i_num in class_iterator:
    print(i_num)

for i_num in squaresGenerator(n):
    print(i_num)

gen = [i ** 2 for i in range(1, n + 1)]
print(gen)
