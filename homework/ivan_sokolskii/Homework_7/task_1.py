target_num = 15
user_input = int(input('Введите число: '))
while True:
    if target_num != user_input:
        print('попробуйте снова')
        user_input = int(input('Введите число: '))
    else:
        print('Поздравляю! Вы угадали!')
        break
