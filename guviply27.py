n=raw_input()
a=' '
for i in n:
	if i.islower():
		a=a+i.upper()
	else:
		a=a+i.lower()
print(a)
