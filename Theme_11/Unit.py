class Unit:
    def __init__(self, name='Воин'):
        self.hp = 100
        self.damage = 20
        self.name = name
        self.alive = True

    def hit_unit(self, unit):
        if self.alive:
            if unit.hp > 20:
                unit.hp -= self.damage
                print('Ударил {}\n У {} осталось {} hp'.format(self.name, unit.name, unit.hp))
            else:
                unit.alive = False
                unit.hp = 0
                print('{} одержал победу'.format(self.name))
