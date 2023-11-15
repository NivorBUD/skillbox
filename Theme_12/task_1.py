class Property:
    def __init__(self, worth):
        self.worth = worth

    def calc_tax(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.tax_percentage = 1.0 / 1_000

    def calc_tax(self):
        return self.worth * self.tax_percentage


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.tax_percentage = 1.0 / 200

    def calc_tax(self):
        return self.worth * self.tax_percentage


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.tax_percentage = 1.0 / 500

    def calc_tax(self):
        return self.worth * self.tax_percentage


property_type = input('Введите тип имущества(квартира, машина, дача): ')
cost = int(input('Введите стоимость имущества: '))
if property_type.lower() in ['квартира', 'машина', 'дача']:
    if property_type.lower() == 'квартира':
        my_property = Apartment(cost)
    elif property_type.lower() == 'машина':
        my_property = Car(cost)
    else:
        my_property = CountryHouse(cost)
    print('Налог на ваше имущество:', my_property.calc_tax())
else:
    print('Ошибка ввода!')
