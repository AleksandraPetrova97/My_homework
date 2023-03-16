# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


numberN = int(input('Введите не превосходящее число:'))
a = 0
number = 0
while number < numberN:
    number = 2**a
    a = a + 1
    if number < numberN:
        print(number)

    

    

