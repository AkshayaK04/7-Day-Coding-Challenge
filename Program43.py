s=input('Enter the string')
print(len(s))


s1=input('Enter the string')
c=0
for x in s1:
	c+=1
print(c)


s2=input('Enter the string')
counter = 0
while s2[counter:]: 
	counter+=1
print(counter)


str=input('Enter the string')
if not str: 
	print(0)
else: 
	some_random_str = 'py'
	print((some_random_str).join(str).count(some_random_str) + 1 )



