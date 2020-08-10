def rverseArray(arr, start, end): 
    while (start < end): 
        temp = arr[start] 
        arr[start] = arr[end] 
        arr[end] = temp 
        start += 1
        end = end-1

def leftRotate(arr, d): 
  
    if d == 0: 
        return
    n = len(arr) 
    rverseArray(arr, 0, d-1) 
    rverseArray(arr, d, n-1) 
    rverseArray(arr, 0, n-1) 
  
def printArray(arr): 
    for i in range(0, len(arr)): 
        print(arr[i],end=" ")

n=int(input('Enter the no. of elements in the list'))
arr=[]
for i in range(0,n):
    c=int(input('Enter the element'))
    arr.append(c)

d=int(input('Enter the no.'))
  
d = d % n       
leftRotate(arr, d) 
printArray(arr) 