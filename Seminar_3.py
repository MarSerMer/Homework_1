# 1 Реализуйте алгоритм перемешивания списка
# import time
# import random
#
# def rand_num (min = 0, max = 10):
#     num = int((time.time()%1)*(max-min)+min)
#     return num
#
# lst = [2,-10,5,8,43]
# #print(random.shuffle(lst))
# print(lst)
#
# for i in range(len(lst)):
#     j = rand_num(0, len(lst)-1)
#     #temp = lst[i]
#     #lst[i] = lst[j]
#     #lst[j] = temp
#     lst[i], lst[j] = lst[j], lst[i] # по сути то же, что и прошлые три строки
#
# print(lst)

# 2 Задайте список. Напишите программу, которая определит, присутствует ли в заданном
# списке строк некое число.

# lst = ['blue', 'green', 'white', 'gr2y', red]
# num = 2
# answer = False
# for i in lst:
#     if str(num) in i: # то же, что и строки 32-33
#         answer = True
#         break
    # for j in i:
    #     if j == str (num):
    #         answer = True
    #         break
#print(answer)

# 3. Напишите программу, которая определит позицию второго
# вхождения строки в списке либо сообщит, что её нет.
#
# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

#lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
lst = ["123", "234", 123, "567"]
fnd = '123'
count = 0
index = -1
for i in range (0, len(lst)-1):
    if lst[i]==fnd:
        count +=1
        if count==2:
            index = i
            break

print (index)