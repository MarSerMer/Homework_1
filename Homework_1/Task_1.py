# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
#
# Пример:#
#  - 6 -> да
#  - 7 -> да
#  - 1 -> нет

day_number = int(input("Please write the day's number to find out if it's weekend:  "))
if (day_number >= 1 and day_number <= 5):
    print("No");
elif (day_number == 6 or day_number == 7):
    print("Yes");
else:
    print("It's not the day's number");
