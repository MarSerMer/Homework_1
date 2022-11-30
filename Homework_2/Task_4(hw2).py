# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

number = int(input('Please enter a number >=3: '))
if (number<3):
    print('Wrong number')
    exit()
list_of_numbers = []
k = -number
for k in range (-number , number+1):
    list_of_numbers.append(k)
    k+=1
print(list_of_numbers)

positions = open('file_for_task_4', 'w')
positions.write('-1\n')
positions.write('0\n')
positions.write('1\n')
positions.write('2\n')
positions.close()

positions = open('file_for_task_4', 'r')
result = 1
for j in positions:
    j = int(j)
    result = result * (list_of_numbers[j])
print(result)

