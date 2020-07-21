n=int(input("Enter the no."))
print('Factors of',n,'are:')
for i in range(1,n):
	if n%i==0:
		print(i)