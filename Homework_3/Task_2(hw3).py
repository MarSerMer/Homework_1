# 2 Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

list_one = [2,3,4,5,6]
#list_one = [2, 3, 5, 6]
list_two = []
for i in range (0, len(list_one)//2):
    list_two.append \
        (list_one[i]*\
        list_one[len(list_one)-1-i])
if (len(list_one)%2 == 1):
    list_two.append((list_one[len(list_one)//2])**2)
print (list_two)