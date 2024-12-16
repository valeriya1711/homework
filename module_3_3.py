def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()                                  # вызов функции без аргументов
print_params(3, 'процент', False)      # вызов функции с тремя аргументами
print_params(100, 'second')               # вызов функции с двумя аргументами и одним по умолчанию
print_params(b='result')                        # вызов функции с одним аргументом и двумя по умолчанию
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [500, 'камень', False]
values_dict = {'a': 7, 'b': 'снег', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [5.12, 'пароль' ]
print_params(*values_list_2, 42)