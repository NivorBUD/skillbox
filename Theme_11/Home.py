import random


class Home:
    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money


class Human:
    def __init__(self, name, home):
        self.name = name
        self.satiety = 50
        self.home = home

    def eat(self):
        self.satiety += 1
        self.home.food -= 1

    def work(self):
        self.home.money += 1
        self.satiety -= 1

    def play(self):
        self.satiety -= 1

    def goToStoreForFood(self):
        self.home.money -= 1
        self.home.food += 1

    def liveTheDay(self):
        cube_num = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.home.food < 10:
            self.goToStoreForFood()
        elif self.home.money < 50:
            self.work()
        elif cube_num == 1:
            self.work()
        elif cube_num == 2:
            self.eat()
        else:
            self.play()

