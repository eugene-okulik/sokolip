def repeat_me(func):
    def wrapper(x, count):
        y_1 = 0
        while y_1 != count:
            print('print me')
            y_1 += 1
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
