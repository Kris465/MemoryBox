my_dict = {
    'dog': 'собака',
    'cat': 'кошка',
    'is': 'есть',
    'good': 'хорошая'
}

eng_text = 'dog is good'
rus_text = ''

for word in eng_text.split():
    if word in my_dict:
        rus_text += my_dict[word] + ' '

print(rus_text)