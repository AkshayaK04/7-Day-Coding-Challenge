a=list(input('Enter the list'))

l=len(a)
t=a[0]
a[0]=a[l-1]
a[l-1]=t

print(a)