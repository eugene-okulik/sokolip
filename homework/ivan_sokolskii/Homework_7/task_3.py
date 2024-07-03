result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'
def print_num(result):
    num_index = result.index(':') + 2
    num = int(result[num_index:])
    num += 10
    print(num)
print_num(result_1)
print_num(result_2)
print_num(result_3)
