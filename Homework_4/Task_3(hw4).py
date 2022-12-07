# 3 Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# - Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]

list_of_numbers = []
def ask_to_enter_numbers_for_the_list():
    a = input("Please enter numbers for the list. \
Push ENTER after every number. You can't enter more than 100 numbers\n When you finish, push SPACE: ")
    return a

for i in range(1,100):
    number = ask_to_enter_numbers_for_the_list()
    if number==' ':
        break
    else:
        list_of_numbers.append(number)

print('So you entered: ', list_of_numbers)

corrected_list = []
for k in list_of_numbers:
    if list_of_numbers.count(k)<2:
        corrected_list.append(k)
print('after deleting all the repeatings we get:', corrected_list)