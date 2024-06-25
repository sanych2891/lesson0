# Домашняя работа по уроку "Условная конструкция.
# Операторы if, elif, else."
# Вводим переменные:

first = input()
second = input()
third = input()

# Вводим условия вычисления и выводим интересующий ответ:

if first == second == third:
    print(3)
elif (first == second or first == third
          or second == third):
    print(2)
else:
    print(0)
# Все исправно работает!
