# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

number = int(input('Plase enter number to get all its prime factors: '))
# найдём все простые числа от 2 до введенного пользователем числа:

prime_numbers = []
for i in range (2, number+1):
    k = 0
    for j in range (1, i+1):
        if i%j == 0:
            k+=1
            if k>2: break
    if k == 2:
            prime_numbers.append(i)
print(f'First 20 prime numbers under the entered number: {prime_numbers[0:20]}')

result_prime_factors = []
while number>1:
    for i in prime_numbers:
        if number%i==0:
            number /=i
            result_prime_factors.append(i)

print (list(set(result_prime_factors)))


