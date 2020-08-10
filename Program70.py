def isMonotonic(A): 
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
  
m=int(input('Enter the no. of elements in the list'))
A=[]
for i in range(0,m):
    c=int(input('Enter the element'))
    A.append(c)
print(isMonotonic(A)) 