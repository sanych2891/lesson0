# Домашняя работа по уроку "Пространство имён"
# Задача "Счётчик вызовов"
# Создать переменную calls = 0 вне функций:
calls = 0
# Создать функцию count_calls и изменять в ней значение
# переменной calls.
# Эта функция должна вызываться в остальных двух функциях.

def count_calls():
    global calls
    calls += 1

# Создать функцию string_info с параметром string
# и реализовать логику работы по описанию.
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

# Создать функцию is_contains с двумя параметрами string
# и list_to_search, реализовать логику работы по описанию.
def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    list_lower = [item.lower() for item in list_to_search]
    return string_lower in list_lower
# Вызвать соответствующие функции string_info и is_contains
# произвольное кол-во раз с произвольными данными.
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
# Вывести значение переменной calls на экран(в консоль).
print(calls)
