#  Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:* 2 2    4 

def sum(number_a, number_b):
    if number_a == 0: 
        return number_b
    if number_b == 0:
        return number_a
    return 1 + 1  + sum(number_a - 1, number_b - 1)


number_a = int(input('Введите первое число: '))
number_b = int(input('Введите второе число: '))

print(sum(number_a, number_b))