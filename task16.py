# print('Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X')

# # Вариант заполнения рандомными числами
# print('Введите количество элементов массива: ')
# elementsarray = int(input())
# import random
# arr = [random.randint(0,10) for _ in range(elementsarray)]
# print('Введите искомое значение X: ')
# print(arr)
# searchentsarrayX = int(input())
# print(arr)
# print(arr.count(searchentsarrayX)) 


 


# # Вариант ввода пользовтелем всего массива

# print('Введите элементы массива через пробел')
# elementsarray = [int(i) for i in input().split()] 
# print('Введите искомое значение X: ')
# searchentsarrayX = int(input()) 
# print(elementsarray)
# print(elementsarray.count(searchentsarrayX)) 