# Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.
# (Не используя библиотеки связанные с рандомом)

import datetime
print(datetime.datetime.now())
rand_number = str(datetime.datetime.now())[-3]
print(rand_number)