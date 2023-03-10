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
arr_copy = arr.copy() # копия

arr_2d = np.array([[5,10,15], [20,25,30], [35,40,45]])
print(arr_2d)
print(arr_2d.shape)
print(arr_2d[0]) # первая строка
print(arr_2d[2]) # последняя строка
print(arr_2d[1][1])
print(arr_2d[1,1])
print(arr_2d[0,2])
print(arr_2d[:2])
print(arr_2d[:2, 1:])
arr = np.arange(1, 11)
print(arr>4)
bool_arr = arr > 4
print(bool_arr)
print(arr[bool_arr])
print(arr)
print(arr[arr > 4])
