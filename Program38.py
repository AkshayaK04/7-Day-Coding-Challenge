n=int(input('Enter the no. of keys in first dictionary'))
m=int(input('Enter the no. of keys in second dictionary'))

d={}
d1={}

print('Enter the details of first dictionary')


for j in range(1,n+1):
	key=input('Enter the key')
	value=input('Enter the value')
	d[key]=value

print('Enter the details of second dictionary')

for j in range(1,n+1):
	keys=input('Enter the key')
	values=input('Enter the value')
	d1[keys]=values

dict={**d,**d1}
print(dict)
	


