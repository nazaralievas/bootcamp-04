# разбор домашки: нужно отсортировать список от большего к меньшему
# способ первый
nums = [4, 6, 7, 99, 34, 12, 8]
nums = sorted(nums) # [4, 6, 7, 8, 12, 34, 99] то есть отсортировали как обычно
print(nums[::-1]) # [99, 34, 12, 8, 7, 6, 4] взяли слайс от начала до конца с шагом -1 то есть в обратном порядке

# способ второй
nums = [4, 6, 7, 99, 34, 12, 8]
nums = sorted(nums, reverse=True) # reverse=True означает сортировать и "отзеркалить?да"
print(nums)



# разбор домашки: перед вами список results с результатами голосования
# сколько всего было кандидатов?
# кто выиграл выборы?
results = ['Trump', 'Biden', 'Bush', 'Trump', 'Bush', 'Biden', 'Biden', 'Biden', 'Trump', 'Biden', 'Bush', 'Trump', 'Bush', 'Biden', 'Biden']

# с помощью функции set() мы превращаем список results в множество чтобы убрать дубликаты:
candidates = set(results)
print(candidates) # {'Trump', 'Biden', 'Bush'}

# с помощью функции len мы узнали длину множества candidates то есть количество кандидатов:
print("Кандидатов всего:", len(candidates))

# а теперь с помощью метода count() посчитаем сколько раз элемент встречается в списке
# results.count('Trump') ---- то есть мы спрашиваем сколько раз Trump встречается в списке results:
print('За Трампа проголосовало:', results.count('Trump'))
print('За Байден проголосовало:', results.count('Biden')) # сколько раз встречается Biden в списке results
print('За Буша проголосовало:', results.count('Bush')) # сколько раз встречается Bush в списке results



# цикл for позволяет нам вывести все элементы списка по очереди:
numbers = [31, 7, 8, 91, 14]
for num in numbers:
    print(num)
# вывод будет такой:
# 31
# 7
# 8
# 91
# 14

# то есть мы пробежадись по списку и каждое число по очереди было в переменной num который мы принтуем
# то есть если мы можем взаимодействовать с каждым элементом списка и например
# проверить каждое число на чётность и вывести  только четные числа:
numbers = [31, 7, 8, 91, 14]
for num in numbers:
    if num % 2 == 0:
        print(num)


# задание: из данного списка выберите возьмите четные числа и добавьте их в список chetnye
numbers = [31, 7, 8, 91, 14]
chetnye = []
for num in numbers:
    if num % 2 == 0:
        chetnye.append(num)

# посмотрим что у нас собралось в списке chetnye
print(chetnye) # [8, 14]



# задание: есть список запрещенных слов
bad_words = ["дурак", "неряха", "лодырь", "невежа", "кикимора"]
# нужно проверить содержит ли комментарий какое-нибудь из запрещённых слов
comment = "ну ты и неряха и кикимора конечно"

# с помощью цикла мы можем пройтись по всему списку плохих слов
# и по очереди поискать каждое плохое слово в комментарии
for word in bad_words:
    if word not in comment:
        pass # если данного плохого слова нет, то идем дальше к следующему слову в списке
    else:
        print("Комментарий содержит запрещенное слово")
        break # если плохое слово есть, то прекращаем дальнейшие поиски


# for i in range
# range переводится как диапазон
# то есть "for i in range" можно перевести как "для i в диапазоне" или "для числа в диапазоне"
# диапазон указываем в скобочках
# первое число это начало
# второе число это конец (если нужны числа до 5, мы пишем 6)
# иногда можно указать третье число: шаг


for i in range(1, 6):
    print(i)

# вывод:
# 1
# 2
# 3
# 4
# 5


# например мы хотим вывести числа от 2 ДО 11 с шагом 2
for i in range(2, 11, 2):
    print(i)

# вывод:
# 2
# 4
# 6
# 8
# 10


# задание: мы решили каждый день деньги по следующей схеме:
# в первый день 1 сом
# во второй день 2 сома
# в третий день 3 сома
# в четвертый день 4 сома
# и так далее 100 дней

# сначала выведем числа от 1 до 100 в консоли
for i in range(1, 101):
    print(i)


# попробуем все эти числа не просто вывести, а сохранить в какой-нибудь сосуд
sosud = []

for i in range(1, 101):
    sosud.append(i)

# и теперь наш sosud выглядит вот так:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# мы уже умеем находить сумму чисел в списке с помощью функции sum()
print(sum(sosud))
# итого за 100 дней мы накопили 5050 сом