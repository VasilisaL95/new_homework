data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

def calculate_structure_sum(*data_structure):
    sum_num = 0
    sum_str = 0

    def sum_func(a):
        nonlocal sum_num
        nonlocal sum_str
        if isinstance(a, int) or isinstance(a, str):
            if isinstance(a, int):
                sum_num += a
            elif isinstance(a, str):
                sum_str += len(a)
        elif isinstance(a, list) or isinstance(a, tuple) or isinstance(a, set):
            for i in a:
                sum_func(i)
        elif isinstance(a, dict):
            for values in a.values():
                sum_func(values)
            for key in a.keys():
                sum_func(key)

    sum_func(data_structure)
    return sum_str + sum_num


print(calculate_structure_sum(data_structure))



#Все числа (не важно, являются они ключами или значениям или ещё чем-то).
#Все строки (не важно, являются они ключами или значениям или ещё чем-то)