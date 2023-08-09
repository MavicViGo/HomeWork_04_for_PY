'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
'''

n = int(input('введите колличество чисел первого множества: '))
m = int(input('введите колличество чисел второго множества: '))
list_1 = []
list_2 = []
import random

for i in range(n):
    list_1.append(random.randint(0, 10))
list_11 = set(list_1)
for i in range(m):
    list_2.append(random.randint(0, 10))
list_22 = set(list_2)

list_res = list_11.intersection(list_22)
print(list_1)
print(list_11)
print(list_2)
print(list_22)
print(sorted(list_res))