max=0
a=input('Enter the first no.')
b=input('Enter the second no.')
c=0

if a>b:
	c=a
else:
	c=b

for x in range(1,c):
	if a%x==0 and b%x==0:
		if x>max:
			max=x

print('The gcd is',max)