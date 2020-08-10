l=list(input('Enter the list'))

max=0

for x in range(0,len(l)):
    c=int(l[x])
    if c>max:
        max=c

print('The largest number is',max)

