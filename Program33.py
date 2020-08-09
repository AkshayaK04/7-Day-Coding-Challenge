d1={}

key=input('Enter the mutiple key values')
value=input('Enter the value')
d1.setdefault(key, []).append(value)

print(d1)


