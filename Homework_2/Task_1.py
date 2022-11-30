# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.(Сделать для строки)
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

# Вариант 1, работает:
chislo_input = input('Введите число: ')
print (chislo_input)
new_chislo = chislo_input.replace(',', '0')
new_chislo = chislo_input.replace('.', '0')
#print (new_chislo)
def split(x):
    return [char for char in x]
#print (split(new_chislo))
chislo_for_count = split(new_chislo)
print (chislo_for_count)

summa = 0
for i in range(0,len(chislo_for_count)):
    chislo_for_count[i] = int (chislo_for_count[i])
    summa += chislo_for_count[i]
print (summa)

#Вариант 2, капризничает
# chislo_input = input('Введите число: ')
# print(type(chislo_input)) # для наблюдения за работой программы и ловли проблем
# print (len(chislo_input)) # для наблюдения за работой программы и ловли проблем
# chislo_step2 = (chislo_input.replace(',','.'))
# chislo_itog = float(chislo_step2)
# print(chislo_itog + 1) # для наблюдения за работой программы и ловли проблем
#
# while chislo_itog%1 > 0:
#     chislo_itog *=10
# print (chislo_itog) # для наблюдения за работой программы и ловли проблем
# summa = 0
# while chislo_itog > 0:
#     ostatok = chislo_itog % 10
#     summa += ostatok
#     chislo_itog //= 10
# print (int(summa))

