# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

from random import randint

lst = [randint(1, 10) for i in range(6)]
print(lst)

sum = 0

for i in range(len(lst)):
    if i % 2 != 0:
        sum = sum + lst[i]
print('Сумма элементов на нечетных позициях: ', sum)