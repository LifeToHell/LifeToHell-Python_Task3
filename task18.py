print('Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X')

elementsarray = int(input('Введите количество элементов массива: '))
import random
arr = [random.randint(0,10) for _ in range(elementsarray)]
arr2 = arr.copy()
print(arr)
searchentsarrayX = int(input('Введите искомое значение X: '))

# вводные данные

for i in range(len(arr)):
  arr[i] -= searchentsarrayX
for i in range(len(arr)):
  if arr[i] < 0:
    arr[i] = -1 * arr[i]
    i += 1

# поиск минимального значения
b = arr.index(min(arr))
print(f'Ближайщее к искомому  числу X = {searchentsarrayX} число: {arr2[b]} c индексом {b}')


