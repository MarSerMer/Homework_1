#1. Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# line_of_numbers = '7 123 654 789 965 432 321 12 0 -5'
# print(type(line_of_numbers))
# print(line_of_numbers)
#
# numbers_list = line_of_numbers.split()
# print(numbers_list)
#
# max = numbers_list[0]
# print(max)
# for i in range(1, len(numbers_list)):
#     if numbers_list[i]>max:
#         max = numbers_list[i]
# print('Наибольшее число:', max)
#
# min = numbers_list[0]
# for i in range(1, len(numbers_list)):
#     if numbers_list[i]<min:
#         min = numbers_list[i]
# print('Наименьшее число:', min)

#2. Найдите корни квадратного уравнения Ax² + Bx + C = 0

koef_A = int(input('Please write A: '))
koef_B = int(input('Please write B: '))
koef_C = int(input('Please write C: '))

diskr = koef_B**2-4*koef_A*koef_C
if diskr<0:
    print('No roots, sorry')
elif diskr==0:
    x = -koef_B/(2*koef_A)
    print ('One root:', x)
else:
    x_1 = round((-koef_B + diskr ** 0.5)/2*koef_A, 2)
    x_2 = round((-koef_B - diskr ** 0.5)/2*koef_A, 2)
    print ('Two roots: ', x_1, 'and', x_2)
