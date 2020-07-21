n=int(input('Enter the number'))
a=n
count=0
while a>0:
	dig=int(a%10)
	count+=1
	a=int(a/10)
	
print(count)

