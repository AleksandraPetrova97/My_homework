# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:* 5  1 2 3 4 5  6  -> 5

from random import randint

number_N = int(input('Введите количество элементов в массиве: '))

massiv_A = [randint(1,10) for i in range(number_N)] 

print(massiv_A)

number_X = int(input("Введите число Х: "))
number = 0
for i in range(number_N):
    if massiv_A[i] == number_X or massiv_A[i] - number_X == 1:
        number = massiv_A[i]


print(number)