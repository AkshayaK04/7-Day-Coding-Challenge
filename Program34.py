n=int(input('Enter the no. of keys'))
d={}
c=1

for i in range(1,n+1):
	key=int(input('Enter the key'))
	value=int(input('Enter the value'))
	d[key]=value
	c+=1

s=sum(d.values())
print(s)