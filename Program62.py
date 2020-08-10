def Punctuation(string): 
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  
    for x in string.lower(): 
        if x in punctuations: 
            string = string.replace(x, "") 
  
    print(string) 
  
string = input('Enter the string')
Punctuation(string) 