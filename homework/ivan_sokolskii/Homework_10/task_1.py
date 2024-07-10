def finish_me(func):
    def wrapper(n):
        func(n)
        print('finished')
    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')
