# Разбор дз
# Создайте список, который содержит квадраты чисел от 1 до 5 с использованием цикла for i in range.
# Создадим пустой список kvadraty
kvadraty = []
for i in range(1, 6):
    kvadraty.append(i ** 2) # i сначала возводим в степень и кидаем в список kvadraty
print(kvadraty) # вот что у нас вышло [1, 4, 9, 16, 25]


# Разбор дз
# Из этого списка выведите только те фрукты, чьё название содержит 7 символов или больше:
fruits = ['banana', 'apple', 'pineaplle', 'apricot', 'orange', 'strawberry']
for fruit in fruits:
    if len(fruit) >= 7:
        print(fruit)


# задание: кого из игроков выбрал и тренер и директор футбольного клуба
trener = ['Mike', 'Kate', 'Luke', 'John', 'Tito']
director = ['Mike', 'Kate', 'Luke', 'Rue', 'Alex']

for player in trener:
    if player in director:
        print(player)


# напришите программу которая принимает от пользователя число и возвращает результат умножения этого числа на числа от 1 до 9
num = int(input('Введите число: '))
for i in range(2, 10):
    print(num * i)


# в списке new_list должны быть фамилии кандидатов без дублирования
# не использовать функцию set
results = ['Trump', 'Biden', 'Bush', 'Trump', 'Bush', 'Biden', 'Trump']
new_list = []

for name in results:
    if name not in new_list:
        new_list.append(name)

print(new_list) # ['Trump', 'Biden', 'Bush']


# while позволяет нам удалить все 2 в списке
# while переводится как "пока"
nums = [2, 1, 3, 2, 4, 5, 6]
while 2 in nums: # то есть мы говорим "пока 2 есть в списке nums"
    nums.remove(2) # удали 2

print(nums) # [1, 3, 4, 5, 6]



# while можно использовать чтобы снова и снова запрашивать пароль у пользователя
parol = 'qwerty'
vvod = input('Введите пароль: ')
while parol != vvod: # пока человек не ввёл парвильный пароль
    vvod = input('Неверный пароль. Попробуйте снова: ')


# давайте дадим пользователю только 3 попытки ввести пароль
parol = 'qwerty'
vvod = input('Введите пароль: ')

popytki = 3 # даём 3 попытки
while popytki > 0: # пока попыток больше нуля
    if vvod != parol: # если пароль введён неправильно
        popytki = popytki - 1 # минусуем одну попытку
        vvod = input('Неверный пароль. Попробуйте снова: ')
    else:
        print('Вы вошли в свой аккаунт')
        break # если пароль введён правильно, то применяем break



# познакомимся со счётчиками и как их кратко записывать
# у нас в копилке уже есть 1000 сом
kopilka = 1000

# мы взносим туда еще денег:
vznos = int(input("положите деньги в копилку: "))

# итого у нас в копилке то что уже было + то что внесли:
kopilka = kopilka + vznos

# эту же запись можно записать вот таким кратким способом, что чаще всего и делают
kopilka += vznos
