vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
s=input('Enter the string')
c=0
for x in range(0,len(s)):
	ch=s[x]
	if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
		c+=1

if c==len(s):
	print('Accepted')
else:
	print('Not Accepted')
  