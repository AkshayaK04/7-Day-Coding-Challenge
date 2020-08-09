n=int(input('Enter the no. of lines'))
for i in range(0,n):
	for a in range(0,i):
		print(' ',end=" ")
	for j in range(i,n):
		print("*",end=" ")
	print('')
		