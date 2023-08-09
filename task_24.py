'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
'''

n = int(input('введите колличество кустов: '))
k = int(input('введите номер куста: '))
list_1 = {}
import random

for i in range(n):
    key = i+1
    list_1[key] = [random.randint(0, 10)]

print(list_1)
if 1 < k < n-1:
    sum_1 = list_1[k-1]+list_1[k]+list_1[k+1]
elif k == n:
    sum_1 = list_1[k-1]+list_1[k]+list_1[k-n+1]
else:
    sum_1 = list_1[n]+list_1[k]+list_1[k+1]
data_2 = list(map(int, sum_1))
print(sum_1)
print(type(data_2))
sum3=0
for i in data_2:
    sum3 = sum3+i
print(sum3)