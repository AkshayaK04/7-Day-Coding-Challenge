n=list(input('Enter the list'))
a=int(input('Enter the index position of the no. to be swapped'))
b=int(input(''))

t=n[a]
n[a]=n[b]
n[b]=t

print(n)