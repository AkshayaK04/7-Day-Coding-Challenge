choice=int(input('Enter the choice: 1 for feet to centimetre and 2 for inches to centimetre'))
n=float(input('Enter the distance'))

if choice==1:
	print(n/30.48)
elif choice==2:
	print(n*2.54)
else:
	print('Invalid')