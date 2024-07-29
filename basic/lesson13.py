# # давайте найдем сумму всех чисел от 1 до 5
# # метод первый - собираем все числа от 1 до 5 в список и затем принтуем сумму этих чисел с помощью функции sum()
# num = 5
# sosud = []
# for i in range(1, num + 1):
#     sosud.append(i)

# print(sum(sosud))


# # метод второй - создадим переменную kopilka к которой будем плюсовать числа от 1 до 5
# num = 5
# kopilka = 0
# for i in range(1, num + 1):
#     kopilka = kopilka + i

# print(kopilka)

# # теперь создадим список с числами от 1 до 5 методом list comprehension
# num = 5
# lst = [i for i in range(1, num + 1)]
# print(sum(lst)) # [1, 2, 3, 4, 5]


# # с помощью list comprehension можно делать всё то, что мы делали с помощью for, range, if
# lst1 = [1, 2, 3, -1, -2]
# lst2 = [num for num in lst1 if num > 0]

# print(lst2) # [1, 2, 3]


# # Рекурсивная функция – это функция, которая вызывает сама себя,
# # и при каждом очередном вызове использует данные, созданные во время предыдущего вызова

# # рекурсию мы рассмотрим через функцию boss_sum, которая,
# # в отличие от втроенной функции sum() может найти сумму даже такого списка:

# geterogen_lst = [-1, 2.5, '4.7', True, [1, [2], 7], {2, 5}, (2,), "word", [[5]]]

# def boss_sum(obj):
#     kopilka = 0
#     for i in obj:
#         if type(i) == int or type(i) == float: # если тип элемента int или float
#             kopilka = kopilka + i # то плюсуем этот элемент к переменной копилка
#         elif type(i) == str or type(i) == bool: # если тип элемента строка то
#             continue # просто перешагиваем этот элемент
#         elif type(i) in [list, set, tuple]: # если тип элемента список или множество или кортеж
#             kopilka = kopilka + boss_sum(i) # то вызываем эту же функцию boss_sum и передаём ему этот элемент. а результат работы этой функции прибавляем к kopilka

#     return kopilka


# print(boss_sum(geterogen_lst))


# # еще одна рекурсивная функция otkryvashka
# # которая при встрече с int принтует его
# # а при встрече с чем-то другим (ожидаем что это что-то другое будет списком) опять вызывает функцию otkryvashka
# def otkryvashka(obj):
#     for i in obj:
#         if type(i) == int:
#             print(i)
#         else:
#             otkryvashka(i)

# lst = [[[[2, 3]]]]
# otkryvashka(lst)

words = ["apple", "banana", "cherry", "date"]
lst = [len(word) for word in words]
print(lst) # [5, 6, 6, 4]


str_numbers = ["1", "2", "3", "4", "5"]
lst2 = [int(num) for num in str_numbers]
print(lst2) # [1, 2, 3, 4, 5]