import numpy as np

mylist = [1,2,3]
print(type(mylist)) # <class 'list'>
print(type(np.array(mylist))) # <class 'numpy.ndarray'>
print(np.array(mylist)) # [1,2,3]

my_arr = np.array(mylist)
print(type(my_arr)) # <class 'numpy.ndarray'>
print(my_arr) # [1 2 3]

my_matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(my_matrix) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(np.array(my_matrix)) #[[1 2 3]
                           #[4 5 6]
                           #[7 8 9]]
print(type(np.array(my_matrix))) # <class 'numpy.ndarray'>
np.arange(0, 3) # создание массива с помощь. numpy
np.zeros((2,3)) # создание массива нулей с плавущей точкой
np.ones((2,3)) # создание массива единиц с плавущей точкой
print(np.linspace(0,10,3)) # получение 3 равностоящих друг от друга чисел
                           # в диапазоне от 0 по 10
print(np.eye(5)) # квадратная матрица [[1. 0. 0. 0. 0.]
                                    #[0. 1. 0. 0. 0.]
                                    #[0. 0. 1. 0. 0.]
                                    #[0. 0. 0. 1. 0.]
                                    #[0. 0. 0. 0. 1.]]

print(np.random.rand(1)) # рандомное число в диапозоне от 0 до 1
print(np.random.rand(5,2)) # матрица рандомных чисед от 0 до 1 с 2 колонками и 5 строками

# Распределение Гауса
print(np.random.randn(2,3)) # числа из стандартного нормально 
                            # распределения, чим ближе к 0 тем больше вероятность

print(np.random.randint(0, 101, 3)) # получение 3 радномных числе в диапозоно от 0 до 101 не включая
print(np.random.randint(0, 101, (2,5)))

#фиксация случайных чисел
np.random.seed(42)
print(np.random.rand(4))
np.random.seed(42)
print(np.random.rand(4))

arr =np.arange(0, 25)
print(arr)
arr2=arr.reshape(5,5)
print(arr2)
ranarr = np.random.randint(0,101,10)
print(ranarr)
print(ranarr.max())
print(ranarr.min())
print(ranarr.argmax()) # индекс максимального числа
print(ranarr.argmin()) # индекс минимального числа
print(ranarr.dtype) # тип данных в масиве
print(arr.shape) # формат массива
arr = arr.reshape(5,5) # изменить формат массива
print(arr.shape)

