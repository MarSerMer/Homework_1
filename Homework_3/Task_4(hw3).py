# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10
from typing import List

number = int(input('Please write number to convert it to binary system: '))
def convert_to_binary (a):
    if a==0:
        return
    else:
        convert_to_binary (a//2)
        print(a % 2, end=" ")

result = convert_to_binary(number)