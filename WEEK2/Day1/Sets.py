#sets are datastructures in python inbuilt 
#storecollection of unique data

cars = {"suzuki", 'Honda', 'Subaru'}
print (cars) 
#get the data type
print(type(cars))

#demonstrate uniqueness
Name = {"livingstone", "marvin", 10, 30, 10}
print(Name)
print(type(Name))

#data duplication
#removes duplicate items
Letters = {'a', 'b', 'c', 'c', 'a', 'a'}
print(Letters) 

#methods 
#Adding elements to the set
Letters.add("z")
print(Letters)

Age = {20, 30, 49, 50}
students = {'brian','Adrian', 'hurdon','William', 49, 50}
#creating union sets 
W = Age.union(students)
print(W)
U = Age.intersection(students)
print(U)
#remove iems from the set
Age.remove(20)
Age.update([21, 45])
print(Age)



