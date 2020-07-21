a=str(input("Enter the sentence"))
a=a+' '
w=''
li=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(0,26):
	l=li[i]
	for j in range(0,len(a)):
		ch=a[j]
		if ch!=' ':
			w=w+ch;
		elif ch==' ':
			c=w[0]
			if c==l:
				print(w,' ')
			w=''
