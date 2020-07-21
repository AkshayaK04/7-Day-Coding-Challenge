m=int(input('Enter the number'))
n=int(input('Enter the number'))

for i in range(m,n+1):
	a=i
	sum=0
	while a>0:
		dig=int(a%10)
		sum+=dig*dig*dig
		a=a/10

	if sum==i:
		print(i)
