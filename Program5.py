n=int(input("Enter the number"))
choice=int(input("please enter ur choice:1 for inches, 2 for yards and 3 for miles"))
print(n)
print(choice)
if choice==1:
	print(n*12)
elif choice==2:
	print(n/3)
elif choice==3:
	print(n/5280)
else:
	print('invalid')