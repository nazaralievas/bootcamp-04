# разбор домашнего задания
imya = input("vvedite imya: ")
familiya = input("vvedite familiyu: ")
print(("Hello, " + familiya + " " + imya + "!!! ") * 5)



# P = 2(a + b) формула вычисления периметра прямоугольника
a = int(input("vvedite dlinu: "))
b = int(input("vvedite shirinu: "))
p = 2 * (a + b)
print("perimetr = ", p)
print("perimetr = " + str(p))



# калькулятор для любых чисел, так как использовали float()
a = float(input("vvedite chislo: "))
b = float(input("vvedite chislo: "))

print("slojenie: ", a + b)
print("vychitanie: ", a - b)
print("umnojenie: ", a * b)
print("delenie: ", a / b)
print("vozvedenie v stepen: ", a ** b)

# вот такое // деление в ответ даёт только целую чать, а дробную выкидывает
# 13 // 2 = 6  то есть если 13 конфет разделить на 2 человек, то каждому достанется по 6
print("delenie nacelo: ", a // b)

# такое % деление наоборот даёт остаток от деления
# 13 % 2 = 1  то есть если 13 конфет разделить на 2 человек то в коробке останется 1 неподелённая конфета
print("ostatok ot deleniya: ", a % b)
