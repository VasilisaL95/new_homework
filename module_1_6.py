my_dict = {'Vasilisa': 1995, 'Dasha': 1998, 'Yulia': '1994'}
print(my_dict)
print(my_dict.get('Dasha'))
print(my_dict.get('Sasha'))
my_dict.update({'Alex': '1986',
                'Oleg': '1987'})
print(my_dict.pop('Vasilisa'))
print(my_dict)

my_set = {3, 5, 7, 5, 7, 3, 8, 8, 8, 3, 'Vasilisa', 'Vasilisa', 'Alex'}
print('Set:', my_set)
my_set.add(1.54)
my_set.add((1,2))
my_set.discard(8)
print('Modified set:', my_set)