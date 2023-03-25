# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
from random import randint
number_elements_one = int(input('Введите количество элементов в первом наборе чисел: '))
number_elements_two = int(input('Введите количество элементов во втором наборе чисел: '))

set_numbers_one = [randint(1, 10) for i  in range(number_elements_one)]
print(f' Первый набор чисел: {set_numbers_one} ')

set_numbers_two = [randint(1, 10) for i  in range(number_elements_two)]
print(f' Второй набор чисел: {set_numbers_two} ')

set_numbers_all = set(set_numbers_one).intersection(set(set_numbers_two))

list(set_numbers_all).sort
print(set_numbers_all)



