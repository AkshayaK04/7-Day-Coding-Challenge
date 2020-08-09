a=list(input('Enter the list'))
x=int(input('Enter the element'))

count=0

for i in range(0,len(a)): 
	if int(a[i])==x:
		count+=1

print('Element is present',count,'times')
