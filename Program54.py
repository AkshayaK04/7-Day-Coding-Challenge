def insertionSort(arr): 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
 
n=int(input('Enter the no. of elements in the list'))
arr = []
for x in range(0,n):
     i=int(input('Enter the element'))
     arr.append(i)
     
insertionSort(arr) 
for i in range(len(arr)): 
    print ("% d" % arr[i]) 