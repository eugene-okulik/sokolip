my_dict = {
    'tuple': (1, 17, "test", False, 22.43, 14),
    'list': [2, 6, True, 14.29, None],
    'dict': {'car' : 'Volvo', 'body' : 'SUV', 'color' : 'Black', 'price' : '12342', 'driver' : 'Boris'},
    'set': {23, 47, False, True, 'name', 55}
}
print(my_dict['tuple'][-1])
my_dict['list'].append(43)
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = 'good'
my_dict['dict'].pop('body')
my_dict['set'].add(590)
my_dict['set'].discard('name')
print(my_dict)
