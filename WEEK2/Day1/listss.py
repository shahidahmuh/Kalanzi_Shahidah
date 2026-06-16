#Used to store ordered collection of items
#Mutable, store data of mulriple data types 

#Creating a list
a = [1,2,3,4,5]
print(a)
print(type(a))

#creating a list using the list constructor
Food = ['pizza', 'posho', 'rice', 'irish']
print(Food)

#Accessing items in a list
print (Food[0])
print(Food[-1])


#Add items to a list
Food.append('chicken')
print(Food)

#Add an item at a specific location
Food.insert(0, "Meat")
print(Food)

#Update elements into a list
#You can replace items with other items
Food[0] = "Ugali"
print(Food)

#Using remove() method to remove items from the lists
Food.remove("chicken")
print(Food)

#How to nest in lists i.e like Matrices or using for loops 