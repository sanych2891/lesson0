# Домашняя работа по уроку
# "Функции в Python.Функция с параметром"
# Задача "Матрица воплоти":

# Оюъявим функцию:
def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        column = []
        for j in range(m):
            column.append(value)
            matrix.append(column)
        return matrix
result_1 = get_matrix(2, 2, 10)

result_2 = get_matrix(3, 5, 42)

result_3 = get_matrix(2, 4, 13)

print(result_1)
print(result_2)
print(result_3)
