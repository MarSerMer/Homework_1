# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*
# *Доп задание: для разного размера уравнения

# Создать файлы, внести в них данные:
# with open('file1_for_task_5.txt', 'w') as data:
#     data.write('2x^3 + 3x^2 - 7x - 2 = 0')
# with open('file2_for_task_5.txt', 'w') as data:
#     data.write('-5x^3 + 6x^2 + 2x - 9 = 0')

# Выцепить данные из файлов, получить строки:
way_1 = open ('file1_for_task_5.txt', 'r')
line_1 = way_1.read()
way_2 = open ('file2_for_task_5.txt', 'r')
line_2 = way_2.read()
way_1.close()
way_2.close()

print (line_1)
print (line_2)


# Работать с полученными строками:
# РАБОТА С ПЕРВОЙ СТРОКОЙ
s_1 = line_1.split() # составлен список строк
s_1_1 = s_1[0:(len(s_1)-2)] # убираем концовку выражения ( = 0 )
# print (s_1)
# print (s_1_1)


koefs_1 = [] # коэффициенты первого выражения
x_list_1 = [] # иксы со степенями первого выражения

if (s_1_1[0]!= '-'): # если первый коэффициент положительный, мы улетим за список в цикле. Чтобы избежать этого,
     s_1_1.insert(0, ' ') # вперед добавляем пробел
for i in range(0, len(s_1_1)-1): #составляем список коэффициентов первого выражения
    if ('x' in s_1_1[i]):
        t = int(s_1_1[i][0:len(s_1_1[i])-3])
        x = s_1_1[i][len(s_1_1[i])-3:]
        if (s_1_1[i-1] == '-'):
            t *= (-1)
        koefs_1.append(t)
        x_list_1.append(x)
if (s_1_1[len(s_1_1)-2] == '-'):
    g = int(s_1_1[len(s_1_1)-1])*(-1)
    koefs_1.append(g)
else:
    g = int(s_1_1[len(s_1_1) - 1])
    koefs_1.append(g)

print('РЕЗУЛЬТАТЫ РАБОТЫ С ПЕРВОЙ СТРОКОЙ: ')
print(koefs_1)
print(x_list_1)
print(' ')

# РАБОТА С ВТОРОЙ СТРОКОЙ
s_2 = line_2.split() # составлен список строк
s_2_2 = s_2[0:(len(s_1)-2)] # убираем концовку выражения ( = 0 )
# print (s_2)
# print (s_2_2)


koefs_2 = [] # коэффициенты второго выражения
x_list_2 = [] # иксы со степенями второго выражения

if (s_2_2[0]!= '-'): # если первый коэффициент положительный, мы улетим за список в цикле. Чтобы избежать этого,
     s_2_2.insert(0, ' ') # вперед добавляем пробел
for i in range(0, len(s_2_2)-1): #составляем список коэффициентов первого выражения
    if ('x' in s_2_2[i]):
        t = int(s_2_2[i][0:len(s_2_2[i])-3])
        x = s_2_2[i][len(s_2_2[i])-3:]
        if (s_2_2[i-1] == '-'):
            t *= (-1)
        koefs_2.append(t)
        x_list_2.append(x)
if (s_2_2[len(s_1_1)-2] == '-'):
    g = int(s_2_2[len(s_2_2)-1])*(-1)
    koefs_2.append(g)
else:
    g = int(s_2_2[len(s_2_2) - 1])
    koefs_2.append(g)

print('РЕЗУЛЬТАТЫ РАБОТЫ С ВТОРОЙ СТРОКОЙ: ')
print(koefs_2)
print(x_list_2)

# РАБОТАЕМ НАД СБОРКОЙ
final_koefs = []
for i in range (0, len(koefs_1)):
    t = str(koefs_1[i] + koefs_2 [i])
    final_koefs.append(t)
print('Итоговые коэффициенты: ', final_koefs)

united_list = []
for i in range(0, len(final_koefs)-1):
    if int(final_koefs[i])<0:
        h = (final_koefs[i]) + x_list_1[i]
    else:
        h = ('+' + final_koefs[i] + x_list_1[i])
    united_list.append(h)
united_list.append(final_koefs[len(final_koefs)-1])
united_list.append(' = 0')

ready_line = str(''.join(united_list))
print('ИТОГОВОЕ ВЫРАЖЕНИЕ:', ready_line)

with open ('file_result_Task_5.txt', 'w') as happy_finish_line:
    happy_finish_line.write(ready_line)