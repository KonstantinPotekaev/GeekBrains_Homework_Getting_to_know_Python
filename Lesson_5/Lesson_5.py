# -*- coding: cp1251 -*-

def task1(text):
    text = list(filter(lambda x: '���' not in x, text.split()))
    return " ".join(text)

text = '������ ��� ��� ����� ���'
print(task1(text))

