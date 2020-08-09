import collections as col
n=int(input('Enter the no. of key values'))
x=input('Enter the key to be printed')

dictionary={}
c=1

while c<=n:
	keys=input('Enter the key')
	values=input('Enter the value')
	dictionary[keys]=values
	c+=1

print(dictionary.get(x,'Element Not present'))