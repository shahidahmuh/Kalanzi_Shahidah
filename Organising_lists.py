cars = ['bmw', 'audi', 'rollsroyce', 'chevoret', 'volkswagen']
print(cars)

#Organizing the list in alphabetical order using sort() method 
cars.sort()
print(cars)
# sorting the list in reverse alphabetical order using reverse=True in the sort() method
cars.sort(reverse=True)
print(cars)
#Sorting a list temporarily using the sorted() function 
#lets you display the list in a particular order but doesn't affect the actual order of the list.
print("\n Here is the original list:")
print(cars)
print("\n")
print("Here is the sorted list:")
print(sorted(cars))

#printing a list in reverse order 
#this reverts the sorted list back to its original order
print("\n")
cars.reverse()
print(cars)

#Finding the length of alist
print("\nthis is the length of the list:") 
print(len(cars))
