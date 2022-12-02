# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint

lst = [randint(1, 10) for i in range(5)]
print(lst)

result = []
if len(lst)%2 == 0:
    for i in range(len(lst)//2):
        result.append(lst[i] * lst[len(lst) - i - 1])

if len(lst)%2 != 0:
    for i in range(len(lst)//2+1):
        result.append(lst[i] * lst[len(lst) - i - 1])
print('Произведения пар чисел: ',result)