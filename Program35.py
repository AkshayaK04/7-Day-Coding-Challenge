n=int(input('Enter the no. of keys'))

d={}
c=1

for i in range(1,n+1):
	key=input('Enter the key')
	value=input('Enter the value')
	d[key]=value
	c+=1

x=input('Enter the element to be removed')
y=input('Enter the element to be removed')

d.pop(x)
del d[y]

print(d)



