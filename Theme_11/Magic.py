class Water:
    def __init__(self):
        self.type = 'Water'

    def __add__(self, other):
        if other.type == 'Air':
            return Storm()
        elif other.type == 'Fire':
            return Steam()
        elif other.type == 'Land':
            return Dirt()
        else:
            return None


class Air:
    def __init__(self):
        self.type = 'Air'

    def __add__(self, other):
        if other.type == 'Fire':
            return Lightning()
        elif other.type == 'Land':
            return Dust()
        else:
            return None


class Fire:
    def __init__(self):
        self.type = 'Fire'

    def __add__(self, other):
        if other.type == 'Land':
            return Lava()
        else:
            return None


class Land:
    def __init__(self):
        self.type = 'Land'


class Storm:
    def __init__(self):
        self.type = 'Storm'


class Steam:
    def __init__(self):
        self.type = 'Steam'


class Dirt:
    def __init__(self):
        self.type = 'Dirt'


class Lightning:
    def __init__(self):
        self.type = 'Lightning'


class Dust:
    def __init__(self):
        self.type = 'Dust'


class Lava:
    def __init__(self):
        self.type = 'Lava'
