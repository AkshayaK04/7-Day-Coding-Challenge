from collections import OrderedDict 
  
def checkOrder(input, pattern): 
    dict = OrderedDict.fromkeys(input) 
    ptrlen = 0 
    for key,value in dict.iteritems(): 
        if (key == pattern[ptrlen]): 
            ptrlen = ptrlen + 1
        
        if (ptrlen == (len(pattern))): 
            return 'true'
  
    return 'false'
    
if __name__ == "__main__": 
    str = input('Enter the string') 
    pattern = input('Enter the pattern')
    print (checkOrder(str,pattern) )