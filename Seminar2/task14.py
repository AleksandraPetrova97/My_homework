# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


numberN = int(input('Введите не превосходящее число:'))
degree = 0
number = 0
for i in range (numberN):
    number = 2**degree
    degree += 1
    if number < numberN:
         print(number, end = ' ')

        
       
    

    

