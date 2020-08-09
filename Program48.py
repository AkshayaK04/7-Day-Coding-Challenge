from collections import OrderedDict 

def removeDup(str): 
    return "".join(set(str)) 

str=input('Enter the string')
 
print("Without duplicate = ",removeDup(str) )

