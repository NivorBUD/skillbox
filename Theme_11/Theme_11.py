from Unit import Unit


print("Задание 1")
unit_1 = Unit('Воин 1')
unit_2 = Unit('Воин 2')
while unit_1.alive and unit_2.alive:
    unit_1.hit_unit(unit_2)
    unit_2.hit_unit(unit_1)

from Student import Student


print("\nЗадание 2")
students = [Student('Вася'), Student('Коля'), Student('Петя'), Student('Ваня'), Student('Вадик'),
            Student('Максим'), Student('Вика'), Student('Настя'), Student('Лена'), Student('Толя')]
students = sorted(students, key=lambda item: item.avgGrade)
for student in students:
    student.print()

from Family import Parent, Kid

print("\nЗадание 3")
kid_1 = Kid('Вася', 10, False, True)
parent_1 = Parent('Коля', 30, [kid_1])
parent_1.calm_kid(kid_1)
parent_1.feed_kid(kid_1)

from Magic import Water, Air, Fire, Land, Storm, Steam, Dirt, Lightning, Dust


print("\nЗадание 4")
water = Water()
air = Air()
fire = Fire()
land = Land()
storm = Storm()
steam = Steam()
dirt = Dirt()
lightning = Lightning()
dust = Dust()

print(water + air)
print(water + fire)
print(water + land)
print(air + fire)
print(air + land)
print(fire + land)

from Home import Home, Human

print("\nЗадание 5")
home = Home()
man_1 = Human('Вася', home)
man_2 = Human('Коля', home)

for i in range(365):
    man_1.liveTheDay()
    man_2.liveTheDay()

print('Сытость первого человека: {}\nСытость второго человека: {}'.format(
    man_1.satiety, man_2.satiety))
print('Денег в доме: {}\nЕды в доме: {}'.format(
    home.money, home.food))

from Game import Game, Board, Cell, Player


print("\nЗадание 6")
player_1 = Player('Коля', 'X')
player_2 = Player('Вася', 'O')

game = Game([player_1, player_2])

game.start_game()

from Matrix import Matrix

print("\nЗадание 7")
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print(m1)
print(m1 + m2)
print(m1 - m2)
print(m1 * m3)
print(m1.transpose())
