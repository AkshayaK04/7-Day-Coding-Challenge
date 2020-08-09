a=list(input('Enter the list'))
x=int(input('Enter the value to be searched'))

count=0

for i in range(0,len(a)):
	if x == int(a[i]) :
		count+=1

print(count)

if count>0:
	print('Element is present',count,'times')
else:
	print('Element is not present')