a=input("Enter a list elements separated by space ")
word=input('Enter the word to be removed')
N=int(input('Enter the value of n'))

l=a.split()

count=0
c=0

for i in range(0, len(l)-1): 
    if l[i] == word: 
        count = count + 1

        if count == N: 
            del(l[i]) 
            c+=1

if c==0:
	print('Error occured-either the value of n is wrong or the wordis not present')
else:
	print(l)


