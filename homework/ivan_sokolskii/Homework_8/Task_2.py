

def progression(limit=100):
    a = 0
    b = 1
    count_1 = 0
    while count_1 < limit:
        yield a
        a = b
        b = a + b
        count_1 += 1


count = 1
for number in progression(100001):
    if count == 5:
        print(number)
    elif count == 200:
        print(number)
    elif count == 1000:
        print(number)
    elif count == 100000:
        print(number)
        break
    count += 1
