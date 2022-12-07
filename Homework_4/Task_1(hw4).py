# Вычислить число Пи c заданной точностью d
#
# Пример:
#
#     - при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10

Pi_number = '3.1415926535'
accuracy = int(input('Please enter number of decimal places you need: '))
if accuracy>0 and accuracy<=10:
    print(Pi_number[0:len(Pi_number)-(10-accuracy)])
else:
    print('Wrong accuracy')