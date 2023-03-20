# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:* 5    1 2 3 4 5    3    -> 1

from random import randint

number_N = int(input('Введите количество элементов в массиве: '))

massiv_A = [randint(1,10) for i in range(number_N)] 

print(massiv_A)

number_X = int(input('Введите число X: '))

summa_number_X = 0

for i in range(number_N):
    if (massiv_A[i] == number_X):
        summa_number_X += 1

print(f'Число {number_X} встречается в массиве: {summa_number_X} раз')        



