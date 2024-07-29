# мы начинаем с вами изучать ООП - объектно ориентированное программирование
# то есть перед тем как делать какой-нибудь сайт, мы рассматриваем сайт как собрание разных объектов
# у которых есть какие-то характерные важные свойства
# на уроке мы представили что создаём конкурента яндекс-такси
# для этого определились с важными классами которые у нас должны быть: пассажир и таксист:


# пишем класс пассажир:
class Passenger:
    def __init__(self, name, phone): # мы решили что у пассажира должны быть имя и номер телефона
        self.name = name # вот эти штуки называются атрибутами
        self.phone = phone # вот эти штуки называются атрибутами


# класс - это шаблон, по которому мы будем создавать ЭКЗЕМПЛЯРЫ класса:
p1 = Passenger('Natalia', '+996778552244')
print(p1.__dict__) # выдаст в консоли {'name': 'Natalia', 'phone': '+996778552244'}


p2 = Passenger('Peter Parker', '0778695123')
print(p2.__dict__) # выдаст в консоли {'name': 'Peter Parker', 'phone': '+0778695123'}



# на уроке вы самостоятельно писали класс Taxist с такими атрибутами как: имя, номер телефона, марка машины, номер машины и стаж вождения (вводим год когда он получил водительские права)
class Taxist:
    def __init__(self, name, phone, marka, car_num, staj):
        self.name = name
        self.phone = phone
        self.marka = marka
        self.car_num = car_num
        self.staj = staj


# и создали экземпляр класса с нужными данными:
t1 = Taxist('Nurbek', '+99677852368', 'Toyota Land Cruiser Prado', '9587AB', 2016)

print(p2.__dict__) # в консоли получили это:
# {'name': 'Nurbek', 'phone': '+99677852368', 'marka': 'Toyota Land Cruiser Prado', 'car_num': '9587AB', 'staj': 2016}



# потом мы решили, что странно в графе стаж видеть 2016, ведь стаж обычно пишется "стаж вождения 9 лет" или "стаж вождения 24 года"
class Taxist:
    def __init__(self, name, phone, marka, car_num, staj):
        self.name = name
        self.phone = phone
        self.marka = marka
        self.car_num = car_num
        self.staj = staj

    # и решилии добавить метод get_real_staj который с помощью модуля datetime выдает текущий год и от него минусует год, в котором таксист получил водительские права
    def get_real_staj(self):
        from datetime import datetime
        datetime.now().year
        real_staj = datetime.now().year - self.staj
        return real_staj

    # и заодно написали метод, который при вызове показывает информацию о таксисте в понятно оформленном виде:
    def __str__(self):
        return f"Ваш водитель: {self.name}, марка машины: {self.marka}, номер машины: {self.car_num}, стаж вождения: {self.get_real_staj()} лет"



# создали экземпляр класса Таксист:
t1 = Taxist('Nurbek', '+99677852368', 'Toyota Land Cruiser Prado', '9587AB', 2016)


# вызвали метод get_real_staj который выдал нам "8", потому что таксист получил права в 2016, значит 2024-2016 = 8 лет водительского стажа
print(t1.get_real_staj())


# и вызвали метож __str__ который красиво расписал всю информацию о таксисте
print(t1.__str__())
# Ваш водитель: Nurbek, марка машины: Toyota Land Cruiser Prado, номер машины: 9587AB, стаж вождения: 8 лет

# и заметьте что тут написано "стаж вождения: 8 лет" потому что мы использовали self.get_real_staj() в 61 строке кода
