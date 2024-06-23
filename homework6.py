# Практическое занятие по теме: "Словари и множества".
# Работа со словарями:
my_dict = {'Alex': 1982, 'Boris': 1986, 'Den': 1978,
           'Semen': 1988, 'Timur': 1989}
print(my_dict)
print(my_dict['Boris'])
my_dict['Oleg'] = 1993
print(my_dict)
my_dict.update({'Sergey': 1990,
                'Ivan': 1987})
print(my_dict)
d = my_dict.pop('Den')
print(my_dict)
print(d)
# Работа с множествами:
my_set = {1, 2, 3, 4, 2, 1, 3, 'God', 'Apple', 'Pen', False, 'God'}
print(my_set)
my_set.update({'Laptop', 8, 9})
print(my_set)
print(my_set.remove('Apple'))
print(my_set)
