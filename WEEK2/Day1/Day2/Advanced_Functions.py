
#Builtin function 
#   LAMBDA FUNCTION
# what is a lambda function
# Is a small anonymous function defined using the keyword lambda: it has one expression
#Syntax; lambda arguments : expression

'''
Key characteristics
-No name(anonymous) 
- Single expression
-Return value automatically
-Can be used where function objects are required

'''

# Lab1 Activity
# Simple Lambda function

Square = lambda x : x*x
print(Square(3))

#Traditional way(function)
def add(x, y):
    return x + y
print (add(3,4))
#Lambda equivalent
add_lambda = lambda x, y: x+y
print(add(3,5))

# Exercise :Write a lambda function to check if the number is even

#Practical Applications
#Lab 2 Activity
#Using lambda with filter

numbers = [4,5,6,7,8,9]
evens = list(filter(lambda x : x % 2 ==0, numbers))
print (evens)

#filter number that is greater than 20
greater_than_20 = list(filter(lambda x: x >20, numbers))
print(greater_than_20)

#Exercise 2 : Using lambda with sorted()function
Fruits = ['Cherry', 'Banana', 'Date', 'Apple', 'Mango', 'DragonFruit']
Sorted_List = sorted(Fruits, key = lambda x : len(Fruits))
print(Sorted_List)

#In descending order
Fruits = ['Cherry', 'Banana', 'Date', 'Apple', 'Mango', 'DragonFruit']
Sorted_List = sorted(Fruits, key = lambda x : len(Fruits), reverse=True)
print(Sorted_List)

# RECURSIVE FUNCTIONS
#Function that calls itself directly or indirectly to solve a problem by breaking it into smaller versions of the same problem
#  e.g fibonacci, factorial, tree traversal
#Components of recursions i.e 
'''
Base Case - the condition that stops the recursion
Recursive case - the the function calls itself 

'''
#Lab3 activity : Factorial Calculation
# 5! = 5 x 4 x 3 x 2 x 1
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))

# Exercise 3 ; using fibonacci using recursion 
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n -1) + fibonacci(n -2)

for i in range(10):
    print(fibonacci(i), end=" ")


# Example 5 : long code for searching binary algorithms
def binary_search(arr, target, left, right):
    #base case- elements that arent found
    if left > right:
        return -1
    
    #find middle
    mid = (left + right) //2

#base case - found target
    if arr[mid] == target:
        return mid
    
#recursive cases - search left 
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    # search right half
    else:
        return binary_search(arr, target, left, mid+1)
    
sorted_array = [1,3,5,7,9,11,13,15]
print("\n")
print(binary_search(sorted_array, 7, 0, len(sorted_array) - 1))



