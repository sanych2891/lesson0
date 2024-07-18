# Дополнительное практическое задание по модулю: "Подробнее о функциях."

# Задание "Раз, два, три, четыре, пять .... Это не всё?":
# Входные данные (применение функции):
# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
# print(result)
# Что должно быть подсчитано:
# 1. Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# 2. Все строки (не важно, являются они ключами или значениям или ещё чем-то)

# Требуемая функция для подсчета содержимого по заданному условию:


def calculate_structure_sum(data_structure):
    def calc_sum(data):
        total_sum = 0 # Начальное число
        if isinstance(data, int):
            total_sum += data # Подсчет целых чисел
        elif isinstance(data, str):
            total_sum += len(data) # Подсчет символов строк
        elif isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
            for sum_item in data:
                total_sum += calc_sum(sum_item) # Подсчет содержимого списков, кортежей, множеств
        elif isinstance(data, dict):
            for key, value in data.items(): # Подсчет значений словарей
                total_sum += calc_sum(key)
                total_sum += calc_sum(value)
        return total_sum # Возврат данных в переменную

    return calc_sum(data_structure) # Возврат данных во вложенную функцию

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35,))}])
]

result = calculate_structure_sum(data_structure)
print(result)
