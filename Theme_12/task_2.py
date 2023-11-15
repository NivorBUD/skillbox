import random


class Simulator:
    __necessaryKarma = 500

    def __init__(self):
        self.karma = 0

    def isWin(self):
        return self.karma >= self.__necessaryKarma

    def one_day(self):
        day_karma = random.randint(1, 7)
        self.karma += day_karma
        lucky_num = random.randint(1, 10)
        if lucky_num == 4:
            random_event = random.randint(1, 5)
            if random_event == 1:
                raise KillError
            elif random_event == 2:
                raise DrunkError
            elif random_event == 3:
                raise CarCrashError
            elif random_event == 4:
                raise GluttonyError
            else:
                raise DepressionError


class KillError(Exception):
    def __str__(self):
        return 'KillError'


class DrunkError(Exception):
    def __str__(self):
        return 'DrunkError'


class CarCrashError(Exception):
    def __str__(self):
        return 'CarCrashError'


class GluttonyError(Exception):
    def __str__(self):
        return 'GluttonyError'


class DepressionError(Exception):
    def __str__(self):
        return 'DepressionError'


karma_exception = open('karma.log', 'w')
simulator = Simulator()
day_num = 1
while True:
    if simulator.isWin():
        break
    try:
        simulator.one_day()
    except Exception as exc:
        karma_exception.write('Day {}: {}'.format(
            day_num, str(exc) + '\n'))
    day_num += 1

karma_exception.close()
