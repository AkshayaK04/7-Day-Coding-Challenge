def partition(arr,low,high): 
    i = ( low-1 )         
    pivot = arr[high]     
  
    for j in range(low , high): 
        if   arr[j] <= pivot:  
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def quickSort(arr,low,high): 
    if low < high:
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

n=int(input('Enter the no. of elements in the list'))
arr = []
for x in range(0,n):
     i=int(input('Enter the element'))
     arr.append(i) 
quickSort(arr,0,n-1) 

print ("Sorted array is:") 
for i in range(n): 
    print ("%d" % arr[i]), 