# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.  Помогите Кате отгадать задуманные Петей числа.




from math import sqrt

summa_numbers = int(input('Введите сумму двух чисел: '))
composition_numbers = int(input('Введите произведение двух чисел: '))

number_X = summa_numbers/2 + sqrt((summa_numbers/2)**2 - composition_numbers)
number_Y = summa_numbers/2 - sqrt((summa_numbers/2)**2 - composition_numbers)

print('Первое загаданное число = ' , round(number_X,2))
print('Второе загаданное число = ' , round(number_Y,2))










