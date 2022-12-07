# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)*
# многочлена и записать в файл многочлен степени k.
#
#     *Пример:*
#
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#     -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0
import random

# *Доп задание: значения коэффициентов от -100 до 100

k = int(input('Please enter K: '))

# ГЛАВА 1: СОСТАВИМ СПИСОК ТОЛЬКО ИКСОВ СО СТЕПЕНЯМИ
def work_with_x_only (k):
    list_of_x = []
    m = 'x^'
    while k >=0:
        list_of_x.append(m+str(k))
        k -= 1
    return list_of_x
first_list = work_with_x_only(k)
print (first_list)

# ГЛАВА 2: СФОРМИРУЕМ КОЭФФИЦИЕНТЫ И ПОСМОТРИМ, ЧТО С НИМИ ДЕЛАТЬ ДАЛЬШЕ:

list_of_koefs = []
for i in range (0, k+1):
    s = random.randint(-100, 100)
    list_of_koefs.append(s)
print(list_of_koefs)

# ГЛАВА 3: СФОРМИРУЕМ СПИСОК ЗНАКОВ
signs_list = []
for i in range(0,k+1):
    if list_of_koefs[i]>0:
        signs_list.append('+ ')
    elif list_of_koefs[i] == 0:
        signs_list.append(' ')
    else:
        signs_list.append('- ')
        list_of_koefs[i] *= (-1)
print(signs_list)

# ГЛАВА 4: ПОПЫТКИ СОБРАТЬ ИЗ ЭТОЙ ГОРЫ СОКРОВИЩ ЧТО-ТО ПРИЕМЛЕМОЕ
semi_final_list = []
for i in range(0,k+1):
    if (list_of_koefs[i]==0):
        continue
    else:
        if i < (k - 1):
            t = signs_list[i] + str(list_of_koefs[i]) + first_list[i] + ' '
        elif i == (k - 1):
            t = signs_list[i] + str(list_of_koefs[i]) + 'x' + ' '
        else:
            t = signs_list[i] + str(list_of_koefs[i]) + ' = 0'
        semi_final_list.append(t)

print(semi_final_list)

text_to_work_with = str(''.join(semi_final_list))

if text_to_work_with[0]=='+':
    text_to_work_with = text_to_work_with[2:]

print(text_to_work_with)

# ГЛАВА 5: ЗАПИСЬ В ФАЙЛ
data = open('File_for_task_4(hw4).txt', 'w')
data.write(text_to_work_with)
data.close