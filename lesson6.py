# Разбор дз: найти среднее арифметическое оценок
biology = int(input("оценка за биологию: "))
litra = int(input("оценка за физику: "))
math = int(input("оценка за математику: "))
chemistry = int(input("оценка за геометрию: "))

srednee = (biology + litra + math + chemistry) / 4
print(srednee)


# разбор домашки: найти количество больших и маленьких букв "s" в тексте
text = "Lorem ipsum dolor sit amet, consectetur adipiscing \
elit, sed do eiusmod tempor incididunt ut labore et dolore \
magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation \
ullamco laboris nisi ut aliquip ex ea commodo consequat. \
Duis aute irure dolor in reprehenderit in voluptate velit \
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint \
occaecat cupidatat non proident, sunt in culpa qui officia \
deserunt mollit anim id est laborym."

# способ первый
print(text.count('s') + text.count('S'))

# способ второй (сначала переводим весь текст в нижний регистр и уже спокойно считаем количество маленьких букв "s")
print(text.lower().count('s'))


# разбор дз: найти нужные буквы и составить фразу "i love python"

# способ первый: с помощью метода find находим индексы нужных букв
print(text.find('i'))
print(text.find('l'))
print(text.find('o'))
print(text.find('v'))
print(text.find('e'))

# и потом принтуем буквы с этими индексами:
print(text[6])
print(text[14])
print(text[1])
print(text[141])
print(text[3])
# и получаем "i l o v e"


# способ второй: всё это впихиваем в один print
print(text[text.find('i')] + ' ' + text[text.find('l')] + text[text.find('o')] + text[text.find('v')] + text[text.find('e')])

# ведь text.find('i') содержит цифру, а значит эту цифру мы можем вставить и использовать как индекс


# -------------------------------------------------------------------------------
# список может быть пустым:
spisok = []

# могут содержать в себе разные типы данных и внутри списка даже может быть другой список:
grades = [4, 5, 3, 'neud', True, 4.5, [1, 2, 7, 9, 0]]

# чтобы вывести нужный элемент, например слово 'neud', нам нужно обратиться к его индексу:
print(grades[3])

# чтобы принтануть внутренний список указываем его индекс
print(grades[6])

# а чтобы принтануть цифру 7 из этого внутреннего списка нужно указать индекс самого списка и индекс этой цифры
print(grades[6][2])


# рассмотрим функции и методы
bally = [5, 4, 5, 3]
print(len(bally)) # длина списка
print(sum(bally)) # сумма всех элементов списка
print(max(bally)) # максимальное число в списке
print(min(bally)) # минимальное число в списке
print(sorted(bally)) # сортировка по возрастанию


students = ['Kate', 'Mike', 'Bob', 'Peter', 'Zuck']
print(sorted(students)) # отсортирует по алфавиту

# если стуенд Bob поменял своё имя на Alan, то указываем его индекс и пишем новое имя
students[2] = 'Alan'

# если хотим добавить еще один элемент с список то используем append
students.append('Thomas')

# если хотим добавить список с несколькими студентами к списку то используем extend
new_students = ['Nick', 'Sara']
students.extend(new_students)

# если хотим вывести список первых трёх студентов то указываем начало и конец
print(students[0:3])

# если хотим вывести последнего студента
print(students[-1])
