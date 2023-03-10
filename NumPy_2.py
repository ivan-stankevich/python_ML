import numpy as np

arr = np.arange(0, 11)
print(arr)
print(arr[8])
print(arr[1:5])
print(arr[:5])
print(arr[5:])

# операции broadCast
arr[0:5] = 100
print(arr)
arr = np.arange(0, 11)
print(arr)
slice_of_array = arr[0:5] # делает срез с массива, но обращается к элементам массива
print(slice_of_array)
print(arr)
slice_of_array[:] = 99 # при изменении меняются и элементы массива
print(slice_of_array)
print(arr)
