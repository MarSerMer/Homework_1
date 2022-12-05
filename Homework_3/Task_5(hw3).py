# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = abs(int(input('Please write number: ')))

fibo = []
for i in range (0, number+1):
    if i==0:
        fibo.insert(0,0)
    elif i == 1:
        fibo.insert(1,1)
    else:
        n = fibo[i-1] + fibo [i-2]
        fibo.append(n)
print (fibo)

f = 0
for k in range (1, number+1):
    if f % 2 == 0:
        fibo.insert(0, fibo[k+f])
    else:
        fibo.insert(0, fibo[k + f]*(-1))
    f+=1

print (fibo)

