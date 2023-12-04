import re

data = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

personal_cars = re.findall(r"[АВЕКМНОРСТУХ][1234567890]{3}[АВЕКМНОРСТУХ]{2}\w{2,3}", data)
taxi_cars = re.findall(r"[АВЕКМНОРСТУХ]{2}[1234567890]{3}\w{2,3}", data)

print("Список номеров частных автомобилей:", personal_cars)
print("Список номеров такси:", taxi_cars)
