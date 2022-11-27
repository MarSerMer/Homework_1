# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
#  - x=34; y=-30 -> 4
#  - x=2; y=4-> 1
#  - x=-34; y=-30 -> 3

zhachenie_x = int(input('Please write x: '));
znachenie_y = int(input('Please write y: '));

if (zhachenie_x > 0 and znachenie_y >0):
    print ("1");
elif (zhachenie_x < 0 and znachenie_y >0):
    print("2");
elif (zhachenie_x < 0 and znachenie_y < 0):
    print("3");
elif (zhachenie_x > 0 and znachenie_y < 0):
    print("4");
else:
    print ('wrong x or y');