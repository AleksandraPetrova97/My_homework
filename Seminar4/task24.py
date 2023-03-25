# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

from itertools import cycle

number_bushes = int(input('Введите сколько кустов на грядке: '))

List = []
for i in range(1, number_bushes + 1):
    List.append(i)

print(List)

summa_max = 0

for i in range(number_bushes + 2):
    summa = sum((List[i:i+3]))
    if summa > summa_max:
        summa_max = summa          

print()
print(f' Максимальная сумма собранных ягод за один раз: {summa_max} ')  

# count_1=int(input("Введите количество элементов 1 набора = "))
# list_1=list(int(input(f" Введите {i} элемент 1 набора = ")) for i in range(count_1))
# count_2=int(input("Введите количество элементов 2 набора = "))
# list_2=list(int(input(f" Введите {i} элемент 2 набора = ")) for i in range(count_2))
# print(list_1)
# print(list_2)
# list_1=set(list_1)
# list_2=set(list_2)
# new_list=list_1.intersection(list_2)
# print(f"Результат = {sorted(new_list)}")


# count=int(input("Введите количество кустов = "))
# list_new=list(int(input(f" Введите количество ягод {i} куста = ")) for i in range(count))
# print(list_new)
# sum_max=list_new[0]+list_new[1]+list_new[count-1]
# number_max=0
# for i in range(1,count):
# if i!=count-1:
# sum_temp=list_new[i]+list_new[i-1]+list_new[i+1]
# else:
# sum_temp=list_new[i]+list_new[i-1]+list_new[0]
# if sum_temp>sum_max:
# sum_max=sum_temp
# number_max=i

# print(f" Максимальная сумма ягод = {sum_max} c {number_max} куста")









