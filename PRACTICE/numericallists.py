#using the range function 
for value in range(1, 10):
    print(value)
    #this only prints the values from 1 to 9 due to te off by one rule in python

#using range to make a list of numbers 
numbers = list(range(1, 6))
print(numbers)  
#this prints the numbers in list form 

#list of even numbers 
even_numbers= list(range(2, 11, 2))
print(even_numbers)  

#list of odd numbers 
odd_numbers= list(range(1,11,2))
print(f"these are odd numbers{odd_numbers}")

#list of square numbers 
squares = []
for value in range (1, 11):
    square = value **2 #you can always skip this and use just "squares.append(value**2)""
    squares.append(square)
    print(square)
    
    #finding the min and max sum of the digits 
digits=[1,2,3,4,5,6,7,8,9,0]
max(digits)
print(max(digits))

#or else you can try writing a list of square numbers 
squares= [value**2 for value in range(1,11)]
print(squares) 

