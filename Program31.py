n=int(input('Enter the no. of key values'))

dictionary={}
c=1

while c<=n:
	keys=input('Enter the key')
	values=input('Enter the value')
	dictionary[keys]=values
	c+=1

print(dictionary)

dictionary_items = dictionary.items()

sorted_items = sorted(dictionary_items)

print(sorted_items)
