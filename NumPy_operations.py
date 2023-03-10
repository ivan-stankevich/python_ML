import numpy as np

arr = np.arange(0,10)
print(arr)
print(arr + 5) # доабвление 5 к каждому элементу массива
print(arr - 2) # отнимаем 2 от каждого элемента массива
print(arr + arr)
print(arr - arr)
print(arr * arr)
print(arr / arr)
print(np.sqrt(arr))
print(np.sin(arr))
print(np.log(arr))
print(arr)
print(arr.sum(), 'сумма')
print(arr.mean(), "среднее значение")  # среднее значение
print(arr.max(), "максимальное число")
print(arr.var(), "дисперсия") # дисперсия
print(arr.std(), "Среднее квадратичное отклонение") # Среднее квадратичное отклонение

arr_2d = np.arange(0, 25).reshape(5,5)
print(arr_2d)
print(arr_2d.shape)
print(arr_2d.sum())
print(arr_2d.sum(axis=0)) # сумма колонок
print(arr_2d.sum(axis=1)) # сумма строк




