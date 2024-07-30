# домашним заданием было создать класс Red с атрибутами name и life
class Red:
    def __init__(self, name, life):
        self.name = name
        self.life = life

# и класс Blue с атрибутами name и life
class Blue:
    def __init__(self, name, life):
        self.name = name
        self.life = life

# при создании экземпляра класса Blue указываем life 100, так как у персонажей игр всегда в начале игры здоровье = 100
blue1 = Blue('Monsterr777', 100)
red1 = Red('Bison111', 100)

# но раз у всех экзепляров класса здоровье будет = 100, может в классе укажем это значение?
class Red:
    life = 100
    def __init__(self, name):
        self.name = name

class Blue:
    life = 100
    def __init__(self, name):
        self.name = name

# и теперь при создании экземпляра класса Blue мы передаём только name, а life у всех экземпляров будет = 100
blue1 = Blue('Monsterr777')
red1 = Red('Bison111')


# как мы видим, классы очень похожи, в таких случаях мы можем наследовать один класс от другого:
class Red:
    life = 100
    def __init__(self, name):
        self.name = name

class Blue(Red):
    pass

# сейчас класс Blue берёт все свои данные у родительского класса Red и у него нет никаких своих атрибутов
# но есть всё родительское
# поэтому мы можем создавать экземпляр класса Blue вот так
blue1 = Blue('Monsterr777')

print(blue2.__dict__) # выведет нам {'life': 100, 'name': 'Godzilla007'}



# но давайте добавим к классу Blue атрибут skill
class Blue(Red):
    def __init__(self, name, skill): # все атрибуты класса Blue
        super().__init__(name) # атрибуты которые наследуются от родителей пишем вот таким образом
        self.skill = skill # атрибут которого нет у родительского класса

# теперь экземпляр класса Blue будем создавать передавая имя, возраст и скилл (навык)
blue1 = Blue('Monsterr777', 'убивать врагов одним ударом')


# теперь давайте напишем метод __str__ в родительском классе Red
class Red:
    life = 100
    def __init__(self, name, age):
        self.name = name
    
    def __str__(self):
        return f'Имя: {self.name}, здоровье: {self.life}'

# в классе Blue этого метода нет, но мы его можем вызвать, так как он есть у родителя
print(blue1.__str__()) # выдаст: Имя: Monsterr777, здоровье: 100


# кстати, данные экземпляра класса можно менять вот так:
blue1.life = 90
blue1.name = 'Ninja666'