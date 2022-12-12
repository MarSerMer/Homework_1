# 1 Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета.
# Играет человек против бота
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# конфеты оппонента достаются сделавшему последний ход.

import random

bunch_of_candies = int(100)
who_is_first_to_take = random.randint(1,2)
print(who_is_first_to_take)
if who_is_first_to_take==1: # let's find out who will take candies first
    print('You begin')
else:
    print('Computer begins')
count = 1
while bunch_of_candies>28:
    print ('Move', count)
    if who_is_first_to_take%2==True: # в этом случае рандом выдал 1, значит, начинает человек
        if count%2==True: # человек будет совершать нечетные ходы
            number = int(input('Enter how many sweets you take (from 1 to 28): '))
            if 0 < number <= 28:
                bunch_of_candies -= number
                count += 1
            else:
                print('No, no, no...really, you can take from 1 to 28 candies at a time. Try again.')
            print('Candies left: ', bunch_of_candies)
        else: # это блок для четного хода, в данном случае это компьютер
            number = bunch_of_candies%29
            if number==0:
                number = random.randint(1, 28)
            print ('Computer takes', number, 'candies. ')
            bunch_of_candies -= number
            count += 1
            print('Candies left: ', bunch_of_candies)
    else: # in this case we get 2 from radom, so the computer begins
        if count%2==True: # computer будет совершать нечетные ходы
            number = bunch_of_candies % 29
            if number == 0:
                number = random.randint(1, 28)
            print('Computer takes', number, 'candies. ')
            bunch_of_candies -= number
            count += 1
            print('Candies left: ', bunch_of_candies)
        else: # это блок для четного хода, в данном случае human's move
            number = int(input('Enter how many sweets you take (from 1 to 28): '))
            if 0 < number <= 28:
                bunch_of_candies -= number
                count += 1
            else:
                print('No, no, no...really, you can take from 1 to 28 candies at a time. Try again.')
            print('Candies left: ', bunch_of_candies)

print('')
if (who_is_first_to_take==1 and count%2==True) or (who_is_first_to_take==2 and count%2==False):
    print ('YOU WIN!! CONGRATULATIONS!')
else:
    print('Computer wins, it seems to be too smart 2day...wanna try again?')