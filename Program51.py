s=input('Enter the string')
k=int(input('Enter the value of k'))
s=s+' '
w=''
for i in range(0,len(s)):
	ch=s[i]
	if ch!=' ':
		w+=ch
	else:
		if len(w)>k:
			print(w)
		w=''