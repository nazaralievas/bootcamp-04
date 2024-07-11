# обычное присваивание переменных:
student1 = "John"
student2 = "Kate"
student3 = "Mike"

# а можно присваивать в один ряд вот так:
student1, student2, student3 = "John", "Kate", "Mike"

# представим, что в стакане 1 у нас чай, а в стакане 2 молоко
# как мы можем поменять местами содержимое стаканов не прибегая к помощи третьего сосуда?
stakan1 = "chai"
stakan2 = "moloko"
# в питоне это можно сделать таким образом:
stakan1, stakan2 = stakan2, stakan1
# теперь в стакане 1 молоко
print(stakan1)



# решение ДЗ про 100-долларовые купюры
som = int(input("Vvedite somy: "))
dollar = som / 86
print("Vy poluchite $100 kupur:", dollar // 100)


# калькулятор с проверкой на ноль
a = float(input("vvedite chislo: "))
b = float(input("vvedite chislo: "))

print("slojenie: ", a + b)
print("vychitanie: ", a - b)
print("umnojenie: ", a * b)
# перед операцией деления мы проверяем является ли второе число нулём и если да, то не делим на ноль
if b == 0: 
    pass
else: # а если нет, то спокойно делим первое число на второе
    print("delenie: ", a / b)

# эта часть кода выполняется независимо от того, равняется второе число нулю или нет так как тут не стоит табуляция (отступ)
print("vozvedenie v stepen: ", a ** b)


# игра угадай число
player1 = int(input("Zagadai chislo ot 0 do 10: "))
player2 = int(input("Otgaday chislo ot 0 do 10: "))

if player1 == player2:
    print("WIN!!!!!")
else:
    print("GAME OVER!")


# проверка роста перед аттракционом
rost = int(input("Vvedite svoi rost: "))
if 150 <= rost <= 200: # проверяем, чтобы рост был выше 150, но ниже 200 сантиметров
    print("Welcome")
else: # если рост ниже 150 или выше 200, то сори, вы не можете кататься на аттракционах
    print("Sorry")



# проверка перед аттракционом на соответствие по росту и по весу
rost = int(input("Vvedite svoi rost: "))
ves = int(input("Vvedite svoi ves: "))

# тут мы используем оператор and (и) то есть если рост выше 150 И ниже 200 см, то человек проходит
if rost >= 150 and rost <=200: 
    if ves < 120: # если рост соответствует нормам, то проверяем вес, чтобы человек был не тяжелее 120 кг
        print("Welcome")
    else:
        print("Ne prohodite po vesu")
else:
    print("Sorry, ne prohodite po rostu")
