text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at," \
       " dignissim vitae libero"
words = []
actual_word = ''
for char in text:
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
add = 'ing'
result_word = []
for word in words:
    if word == ',' or word == '.':
        result_word.append(word)
    else:
        result_word.append(word + add)
final_text = (' '.join(result_word))
clear_text = final_text.replace(" ,", ",")
clear_text_1 = clear_text.replace(" .", ".")
print(clear_text_1)
