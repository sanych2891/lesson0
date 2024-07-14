# Самостоятельная работа по уроку "Рекурсия"
# Задача "Рекурсивное умножение цифр":

# Напиши функцию get_multiplied_digits, которая принимает
# аргумент целое число number и подсчитывает произведение цифр этого числа.

# Решение:
# Напишите функцию get_multiplied_digits и параметр number в ней.

def get_multiplied_digits(number):
        number = int(number) # отсечем нули в начале числа
        str_number = str(number)
        first = int(str_number[0])

        while str_number.endswith('0'):  # отсечем нули и в конце числа, тобы было корректное умножение
            str_number = str_number[:len(str_number) - 1]
        if len(str_number) > 1:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            return first

number = input('Введите целое число: ')
# print(f'Произведение цифр числа {number} :', get_multiplied_digits(number))
