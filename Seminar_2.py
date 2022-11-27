# 3 Для натурального n создать словарь индекс-значение, состоящий из
# элементов последовательности 3n+1
# Пример:
# Для n = 6: {1:4, 2:7, 3:10, 4:13, 5:16, 6:19}
#n = int(input('Введите N: '))
#n_list = {}
# #for i in range(1,n+1):
# #    n_list[i] = 3*i+1;
#
# n_list = {i: 3*n+1 for i in range (1,n+1)}
# print(n_list)
#
# #4 Напишите программу, в которой пользователь будет
# # задавать 2 строки, а программа - опреедлять
# # количество вхождений одной строки в другую.
#
# str_1 = input('Введите первую строку')
# str_2 = input('Введите вторую строку')
#
# str_1_arr = str_1.split()
# count = 0
# for i in str_1_arr:
#     if i.lower() == str_2.lower()
#         count+=1
# print(count)

# ИЛИ ТАК:
# print(str_1.count(str_2))

# 5 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# chislo = int(input("Введите число"))
# summa = 0
# while chislo > 0:
#     ostatok = chislo % 10
#     summa +=ostatok
#     chislo //= 10
# print (summa)

chislo = float(input("Введите число: "))
while chislo%1 !=0:
    chislo *=10
summa = 0
while chislo > 0:
    ostatok = chislo % 10
    summa +=ostatok
    chislo //= 10
print (int(summa))
