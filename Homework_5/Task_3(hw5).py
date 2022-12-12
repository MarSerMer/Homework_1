# 3 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

isolda = 'aaFFFFaaAAABnnnMMMMnnnMFfA'
isolda = isolda + ' '
result_str = ''

while len(isolda) > 1:
    count = 1
    h = isolda[0]
    while isolda[0] == isolda[1]:
        count += 1
        isolda = isolda[1:]
    isolda = isolda[1:]
    result_str = result_str + str(count) + h
print (result_str)


