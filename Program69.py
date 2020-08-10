def construct(n, m, a): 
    ind = 0

    for i in range(n): 
        if (a[i]!=-1): 
            ind = i 
            break

    for i in range(ind-1, -1, -1): 
        if (a[i]==-1): 
            a[i]=(a[i + 1]-1 + m)% m 
  
    for i in range(ind + 1, n): 
        if(a[i]==-1): 
            a[i]=(a[i-1]+1)% m 
    print(*a) 
  
n=int(input('Enter the no. of elements in the list'))
a=[]
for i in range(0,n):
    c=int(input('Enter the element'))
    a.append(c)

m=int(input('Enter the no.'))
construct(n, m, a) 