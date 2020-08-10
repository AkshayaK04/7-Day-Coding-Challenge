def findremainder(arr, lens, n): 
    mul = 1

    for i in range(lens):  
        mul = (mul * (arr[i] % n)) % n 
      
    return mul % n 

lens=int(input('Enter the no. of elements in the list'))
arr=[]
for i in range(0,lens):
    c=int(input('Enter the element'))
    arr.append(c)

n=int(input('Enter the no. to be divided by'))
  
print( findremainder(arr, lens, n)) 