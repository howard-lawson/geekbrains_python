"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.

Например: 20м*5000м*25кг*5см = 12500 т

"""


class Road:
    def __init__(self, length, width, weight, thickness):
        self.length = length
        self.width = width
        self.weight = weight
        self.thickness = thickness

    def calc(self):
        total = self.length * self.width * self.weight * self.thickness / 1000
        print(f'Потребуется {total} тонн')


c_item = Road(20, 5000, 25, 5)
c_item.calc()
