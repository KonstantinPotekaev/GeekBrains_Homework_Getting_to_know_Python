# -*- coding: cp1251 -*-

def task1(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = 'абвгде ооо грг ввраи абв'
print(task1(text))

