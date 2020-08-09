import re 

def run(string): 
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 

    if(regex.search(string) == None): 
        print("String has no special character") 
          
    else: 
        print("String has special character") 
      
string = input('Enter the string')

run(string) 
