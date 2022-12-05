# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
#     - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19

list_of_floats = [1.1, 1.2, 3.1, 5.1, 10.01]
list_of_tails = []
for i in range(0, len(list_of_floats)):
    list_of_tails.append(round((list_of_floats[i]%1), 2))
print (list_of_tails)

max = list_of_tails[0]
for j in range(1,len(list_of_tails)):
    if (list_of_tails[j]>max):
        max = list_of_tails[j]

min = list_of_tails[0]
for k in range(1,len(list_of_tails)):
    if (list_of_tails[k]<min):
        min = list_of_tails[j]
print(max-min)