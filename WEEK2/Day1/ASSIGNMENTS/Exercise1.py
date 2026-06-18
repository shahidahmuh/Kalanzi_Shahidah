#LISTS
Names = ["Aida", "Hassan", "Muhammad", "Pearl", "Liz"]
print(Names)
#1 Print the 2nd item
print(Names[1]) 

#2 Change the value of the first item to a new value
Names.insert(0, 'Agnes')
print(Names)

#3 Add a 6th item
Names.append("Kourtney")
print(Names)

#4 Add "Bathel" as the 3rd item in the list
Names.insert(2, "Bathel")
print(Names)

#5 Remove the 4th item from the list 
Names.pop(3)
print(Names)

