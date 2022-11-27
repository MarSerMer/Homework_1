# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
#
# Пример:
#  - A (3,6); B (2,1) -> 5,09
#  - A (7,-5); B (1,-1) -> 7,21

dot1_x = int(input("Please write x coordinate of the first dot: "));
dot1_y = int(input("Please write y coordinate of the first dot: "));
dot2_x = int(input("Please write x coordinate of the second dot: "));
dot2_y = int(input("Please write y coordinate of the second dot: "));

print (round(((dot1_x-dot2_x)**2 + (dot1_y-dot2_y)**2)**0.5, 2));