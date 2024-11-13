def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = (25, "hello", [4, 5, 6])
values_dict = {'a': "world", 'b': 45, 'c': False}
values_list_2 = [54.32, 'Строка']


print_params()
print_params(4, c = 7)
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)