# домашним заданием было написать класс Poezdka:
class Poezdka:
    def __init__(self, marshrut, time_start, stoimost, taxist, passenger):
        self.marshrut = marshrut
        self.time_start = time_start
        self.stoimost = stoimost
        self.taxist = taxist
        self.passenger = passenger

# и когда мы создаём экземпляр класса Poezdka, непонятно что писать на месте ткасист и пассажир
poezdka1 = Poezdka('7 mrkn - Dordoi', '08:30', 400, '???', '???')

# мы можем создать экземпляры классов Passenger (p3) и Taxist (t1)
class Passenger:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

p3 = Passenger('Sergei', '+700345678')

class Taxist:
    def __init__(self, name, phone, marka, car_num, staj):
        self.name = name
        self.phone = phone
        self.marka = marka
        self.car_num = car_num
        self.staj = staj

t1 = Taxist('Marat', '+99677852368', 'Honda Fit', '9587AB', 2020)

# и вставить их сюда
poezdka1 = Poezdka('7 mrkn - Dordoi', '08:30', 400, t1, p3) # <-- вот

# и теперь мы можем узнать имя пассажира
print(poezdka1.passenger.name)

# и имя таксиста
print(poezdka1.taxist.name)

# ------------------------------------------------------------------------

# давайте теперь доделаем класс Taxist
# помните мы хотели добавить к нему атрибут "рейтинг"
# рейтинг у нас будет атрибутом в виде пустого списка, куда мы собираем все оценки от пассажиров и выводим среднее арифметическое
class Poezdka:
    def __init__(self, marshrut, time_start, stoimost, taxist, passenger):
        self.marshrut = marshrut
        self.time_start = time_start
        self.stoimost = stoimost
        self.taxist = taxist
        self.passenger = passenger
        self.rating = []
    
    # добавим метод add_rating в которую будем писать оценку и эта оценка будет добавляться в наш self.rating = []
    def add_rating(self, ocenka):
        self.rating.append(ocenka)


# вот наш таксист:
t1 = Taxist('Nurbek', '+99677852368', 'Toyota Land Cruiser Prado', '9587AB', 2016)

# и вот такие оценки ему поставили:
t1.add_rating(5)
t1.add_rating(3)
t1.add_rating(4)
t1.add_rating(5)

# давайте посмотрим собираются ли эти оценки в списочке таксиста
print(t1.rating) # вот что увидим в консоли [5, 3, 4, 5] то есть список пополняется

# теперь нам надо высчитать среднее арифметическое
# среднее ариф. мы высчитывали так: сумму чисел делили на количество чисел. давайте вспомним как:
lst = [5, 3, 4, 5]
print(sum(lst) / len(lst))

# окей, внедрим эту логику в класс Taxist
class Taxist:
    def __init__(self, name, phone, marka, car_num, staj):
        self.name = name
        self.phone = phone
        self.marka = marka
        self.car_num = car_num
        self.staj = staj
        self.rating = []

    def add_rating(self, ocenka):
        self.rating.append(ocenka)
    
    def get_rating(self):
        return sum(self.rating) / len(self.rating) # сумму всех поставленных оценок разделили на их количество


# обратившись к этому методу увидим средний рейтинг: 4.25
print(t1.get_rating())


# давайте теперь допишем наш метод __str__ и добавим туда инфу о рейтинге водителя
class Taxist:
    def __init__(self, name, phone, marka, car_num, staj):
        self.name = name
        self.phone = phone
        self.marka = marka
        self.car_num = car_num
        self.staj = staj
        self.rating = []

    def add_rating(self, ocenka):
        self.rating.append(ocenka)
    
    def get_rating(self):
        return sum(self.rating) / len(self.rating)

    def get_real_staj(self):
        from datetime import datetime
        datetime.now().year
        real_staj = datetime.now().year - self.staj
        return real_staj
    
    def __str__(self):
        return f"Ваш водитель: {self.name}, марка машины: {self.marka}, номер машины: {self.car_num}, \
стаж вождения: {self.get_real_staj()} лет, рейтинг: {self.get_rating()}"
