class Parent:
    def __init__(self, name, age, children):
        self.name = name
        self.children = children
        min_age = 16 + min([kid.age for kid in children])
        if age >= min_age:
            self.age = age
        else:
            print('Возраст слишком мал для возраста детей')
            while age < min_age:
                age = int(input("Введите другой возраст: "))
            self.age = age

    def get_info(self):
        return 'Имя:{}\nВозраст:{}\nСписок детей:{}\n'.format(
            self.name, self.age, ' '.join(self.children)
        )

    def calm_kid(self, kid):
        if kid.is_calm:
            print('{} и так спокоен'.format(kid.name))
        if kid in self.children:
            kid.is_calm = True
            print('Теперь {} спокоен'.format(kid.name))
        else:
            print('Это не мой ребёнок!')

    def feed_kid(self, kid):
        if not kid.is_hungry:
            print('{} и так сыт'.format(kid.name))
        if kid in self.children:
            kid.is_hungry = False
            print('Теперь {} сыт'.format(kid.name))
        else:
            print('Это не мой ребёнок!')


class Kid:
    def __init__(self, name, age, is_calm, is_hungry):
        self.name = name
        self.age = age
        self.is_calm = is_calm
        self.is_hungry = is_hungry