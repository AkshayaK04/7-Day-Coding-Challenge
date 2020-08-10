def splitArr(arr, n, k):  
    for i in range(0, k):  
        x = arr[0] 
        for j in range(0, n-1): 
            arr[j] = arr[j + 1] 
          
        arr[n-1] = x 

n=int(input('Enter the no. of elements in the list'))
arr=[]
for i in range(0,m):
    c=int(input('Enter the element'))
    arr.append(c)

position=int(input('Enter the position'))       
  
splitArr(arr, n, position) 
  
for i in range(0, n):  
    print(arr[i], end = ' ') 