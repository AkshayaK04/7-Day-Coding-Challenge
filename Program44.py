s=input('Enter the string')
s=s+' '
w=''
for i in range(0,len(s)):
	ch=s[i]
	if ch!=' ':
		w+=ch
	else:
		if len(w)%2==0:
			print(w)
		w=''