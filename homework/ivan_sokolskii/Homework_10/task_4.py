PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

words = []
actual_word = ''
for char in PRICE_LIST:
    if char.isalpha():
        actual_word += char
    else:
        if actual_word:
            words.append(actual_word)
            actual_word = ''
        if char == ',' or char == '.':
            words.append(char)
if actual_word:
    words.append(actual_word)
new_words = list(filter(lambda x: x != 'р', words))
number = []
actual_number = ''
for char in PRICE_LIST:
    if char.isnumeric():
        actual_number += char
    else:
        if actual_number:
            number.append(actual_number)
            actual_number = ''
        if char == ',' or char == '.':
            number.append(char)
if actual_number:
    number.append(actual_number)
number = [int(x) for x in number]
finish_dict = dict(zip(new_words, number))
print(finish_dict)
