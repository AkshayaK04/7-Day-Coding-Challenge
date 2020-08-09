from operator import itemgetter

n=int(input('Enter the no. of dictionaries'))

d1=[]

for j in range(1,n+1):
	d={}
	key='name'
	v1=input('Enter the name')
	d[key]=v1
	k='age'
	value=input('Enter the age')
	d[k]=value
	d1.append(d)
		
print('The list sorted by age:')
print(sorted(d1,key=itemgetter('age')))