def leftRotate(arr, d, n): 
    for i in range(gcd(d,n)):  
        temp = arr[i] 
        j = i 
        while 1: 
            k = j + d 
            if k >= n: 
                k = k - n 
            if k == i: 
                break
            arr[j] = arr[k] 
            j = k 
        arr[j] = temp 
    
def printArray(arr, size): 
    for i in range(size): 
        print ("%d" % arr[i], end=" ") 
   
def gcd(a, b): 
    if b == 0: 
        return a; 
    else: 
        return gcd(b, a%b) 

m=int(input('Enter the no. of elements in the list'))
arr=[]
for i in range(0,m):
    c=int(input('Enter the element'))
    arr.append(c)

d=int(input('Enter the 2 nos.'))
n=int(input(''))
print('The original array is')
print(arr)
leftRotate(arr, d,n)
print('The rotated array is:')
printArray(arr, n) 
