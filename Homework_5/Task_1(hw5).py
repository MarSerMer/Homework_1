# 1 Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
# b) Подумайте, как наделить бота ""интеллектом""



# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Нужно взять остаток от деления на 29


import random

bunch_of_candies = int(100)
who_is_first_to_take = random.randint(1,2)
print(who_is_first_to_take)
if who_is_first_to_take==1:
    print('Player 1 begins')
else:
    print('Player 2 begins')
count = 1
while bunch_of_candies>28:
    print('Move', count)
    number = int(input('Enter how many sweets you take (from 1 to 28): '))
    if 0<number<=28:
        bunch_of_candies -= number
        count += 1
    else:
        print('No, no, no...really, you can take from 1 to 28 candies at a time. Try again.')
    print('Candies left: ', bunch_of_candies)

print(' ')

if (who_is_first_to_take==1 and count%2==True) or (who_is_first_to_take==2 and count==False):
    print ('Player 1 wins. Congrats!!')
else:
    print('Player 2 wins. Congrats!!')


