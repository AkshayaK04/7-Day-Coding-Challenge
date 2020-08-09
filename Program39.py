n=int(input('Enter the no. of students'))

d1=[]

for j in range(1,n+1):
	d={}
	key='name'
	value=input('Enter the name')
	d[key]=value
	k1='sub1'
	v1=input('Enter the marks of sub1')
	d[k1]=v1
	k2='sub2'
	v2=input('Enter the marks of sub2')
	d[k2]=v2
	k3='sub3'
	v3=input('Enter the marks of sub3')
	d[k3]=v3
	k='score'
	score=(int(d[k1]+d[k2]+d[k3]))/3
	d[k]=score
	s='grade'
	if score>=90:
		grade='A'
	elif score>=80:
		grade='B'
	elif score>=70:
		grade='C'
	else:
		grade='D'
	d[s]=grade
	d1.append(d)

print(d1)


