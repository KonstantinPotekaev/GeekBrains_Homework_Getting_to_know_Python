# -*- coding: cp1251 -*-

def encode(s):
	encoding = ''
	i = 0
	while i < len(s):
		count = 1
		while i + 1 < len(s) and s[i] == s[i + 1]:
			count = count + 1
			i = i + 1
		if(count>1):
			encoding += str(count)
		encoding += s[i]
		i = i + 1

	return encoding


def decoding(s):
	n = 1
	res = ''
	for i in range(len(s)):
		if (s[i].isdigit()):
			n = int(s[i])
		else:
			res+= s[i] * n
			n = 1
	return res

text = encode('Привеееет, меня зовут Константин!')
print(text)

print(decoding(text))