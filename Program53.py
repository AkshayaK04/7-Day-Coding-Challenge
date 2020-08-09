def search(arr, x): 
  
    for i in range(len(arr)): 
  
        if arr[i] == x: 
            return i 
  
    return -1

arr=list(input('Enter the list'))
x=input('Enter the value of x')

r=search(arr,x)

if r!=-1:
	print('The element is present at the index position of',r)
else:
	print('The element is not present')