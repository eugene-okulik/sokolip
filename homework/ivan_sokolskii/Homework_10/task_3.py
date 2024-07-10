

def function(func):
    def wrapper(first, second):
        if first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif second > first:
            return func(first, second, '/')
        if first < 0 or second < 0:
            return func(first, second, '*')
    return wrapper


@function
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return second - first
    elif operation == '/':
        return first / second
    if operation == '*':
        return first * second


first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
result = calc(first, second)
print(result)
