# Самостоятельная работа по уроку
# "Распаковка позиционных параметров".

# Домашнее задание по уроку "Распаковка позиционных параметров".
# Задача "Распаковка":


# 1. Функция с параметрами по умолчанию:
def print_params(a = 1, b ='строка', c = True):
    print(a,b,c)
print_params()
print_params(b = 25)
print_params(c=[1,2,3])
# print_params(1,2,3,4) - ошибка

# 2. Распаковка параметров:
values_list = [1,'abrakadabra',False]
values_dict = {'a': 2981, 'b': 1982, 'c': 21}
print_params(*values_list)
print_params(**values_dict)

# 3. Распаковка + отдельные параметры:
values_list_2 = [117.84, 'Hello' ]
print_params(*values_list_2, 82)
