n=int(input('Enter the value of n'))
i=0
j=1
a=3
sum=1
while a<=n:
	s=i+j
	sum+=s
	i=j
	j=s
	a+=1

print(sum)