#Loops in python
#these are programming constructs that allow you to repeat a block of code multiple times.

#loops are used to perform repititive tasks without having to write the same code multiple times.

#For Loop 
for day in range(1,6):
    print(f'Day {day}: Python')

#Real world examples
fruits = ["apples", "banana", "oranges"]
for fruit in fruits:
    print (f"i like {fruit}")

#Exercise 1
#Count from 1 - 10 using for loops 
for numbers in range(0,11):
    print(numbers)

#Exercise 2
#Loop through a string and print each character (e.g. "i Love Python")
characters = 'I love Python'
for character in characters:
    print (character)

#While Loop 
#allows you to repeat a condition as long as it is true 

#Exercise 3 ; write a program that demonstrates a bank balance 

Balance = int(input("Enter Balance:"))



while Balance > 0:
    print(f"current balance: ${Balance}")
    action  = input("Do you want to deposit or withdraw? :")
    if action == "deposit":
        Deposit = int (input("Enter deposit amount:"))
        Amount= Balance + Deposit
        print(Amount)
    elif action == "withdraw":
        Withdraw = int (input("Enter Withdraw amount:"))
        if Amount > Balance:
            print("Insufficient Funds!!!!") 
        else:
            Amount = Balance - Withdraw 
        print(Amount)
    else:
        print("Insufficient Funds!!!!" )




#Nested Loops - a loop inside another loop 
#example multiplic
for i in range (1,5):
    for j in range(i):
        print("*", j)

# exercise 4 Write a program that uses nested loops too print a pattern of numbers 
for i in range (0,5):
    for j in range(i):
        print(j)
    print()

