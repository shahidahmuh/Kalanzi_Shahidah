
#learning how to write lists in python
bicycles = ['trek', 'redline', 'specialised', 'everything']
print(bicycles)
# acessing the elements in the lists separately
print(bicycles[0])
#you can also add some methods to the value 
print(bicycles[2].upper())
#accessing the last element in the list in python has a specialised syntax
print(bicycles[-1])#this might help when we are dealing with stacks and other datastructures

#using individual values in a list
message= f"My first bicycle was a {bicycles[1].upper()}."
print(message)

#modifying a value in the list 
bicycles[-1] = 'English'
print(bicycles)
#adding a new item to the list by appending the list 
bicycles.append('Germany')
print(bicycles)

#inserting a value at any position in the list
bicycles.insert(0, 'bugati')#this shifts every other value in the list to the right
print(bicycles)
#deleting an item from a known index in the list
del bicycles[0]

#removing an  item using the pop()method this helps remove an item that you have just input 
#the pop()lets you work with the item even after removing it 
#assign the value to the variable 
popped_bicycle = bicycles.pop()
print(bicycles)
#since you had assigned the value a varible so you can acess it even after popping it
print(popped_bicycle)

#poping an item from any position in the list 
first_owned = bicycles.pop(0)
print(f"the first bicycle i ever owned was a {first_owned.title()}")

#removing an item by value from the list
bicycles.remove('specialised')
print(bicycles)

bicycles.insert(-1, 'redline')
print(bicycles)

bicycles.remove('redline')
print(bicycles)
