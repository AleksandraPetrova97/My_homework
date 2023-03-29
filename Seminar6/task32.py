# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


from random import randint

def index_element(list_n, minimum, maximum):
    for i in range(len(list_n)):
        if minimum <= list_1[i] <= maximum:
            print(i, end= " ")
     
list_1 = [randint(1,10) for i in range(int(input('Введите количество элементов списка: ')))]

print(list_1)

number_minimum = int(input('Введите минимальное число в диапазоне: '))
number_maximum = int(input('Введите максимальное число в диапазоне: '))

index_element(list_1, number_minimum, number_maximum)




