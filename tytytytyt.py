# grades = [4, 5, 3, 'neud', True, 4.5, [1, 2, 7, 9, 0]]

# print(grades[6][1])
# print(grades[3].upper())
# print(len(grades))

# bally = [5, 4, 5, 3]
# bally[3] = 4
# print(bally)
# bally.remove(5) # указываем не индекс, а сам элемент который хотим удалить
# deleted = bally.pop(-1) # указываем индекс элемента который хотим удалить и этот
# print('Вы только что удалили:', deleted) # с помощью pop() мы  можем удалить э
# print(bally)
# print(sum(bally) / len(bally))
# print(max(bally))
# print(min(bally))
# print(sorted(bally))
# print(bally)
# print(bally.reverse())
# print(bally)

student = ['Kate', 'Mike', 'Bob']
print(sorted(student))
print(student[0:2])

student[2] = 'Alan'

student.append('Thomas') # append позволяет нам добавлять один элемент в список
new_student = ['Nick', 'Sara']
student.extend(new_student) # extend позволяет добавлять список к списку

print(student)
