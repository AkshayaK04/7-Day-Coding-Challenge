s=str(input('Enter the word'))
a=0
e=0
i=0
o=0
u=0
for j in range(0,len(s)):
	ch=s[j]
	if ch=='a':
		a+=1
	if ch=='e':
		e+=1
	if ch=='i':
		i+=1
	if ch=='o':
		o+=1
	if ch=='u':
		u+=1

print('a=',a)
print('e=',e)		
print('i=',i)
print('o=',o)
print('u=',u)