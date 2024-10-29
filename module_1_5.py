immutable_var = ('apple', 1,2, True)
print(immutable_var)

# immutable_var[2] = 4
# TypeError: 'tuple' object does not support item assignment
# Кортеж относится к неизменяемым типам данных.
# Невозможно изменить содержимое кортежа.

mutable_list = ('apple', [1,2,3,4], True)
print(mutable_list)
mutable_list[1][0] = 5
print(mutable_list)

