total = 0
count = 0
while count < 5:
   number = int(input("Enter number:"))
   total += number
   count += 1
average = total/5
print("Average is :", average)


#input function is used to take user input i.e input()
age = int(input("Enter your age:"))
if age >= 18 :
    print ("you are eligible")
else:
    print ("you are not eligible")

#using the formatted output method


secretcode =int(input("provide secret code:"))
count = 0
while count < 3:
    guess = int(input("guess the number:"))
    if guess == secretcode:
       print(f"Correct!{secretcode}")
       break
    count += 1
if count == 3 and guess != secretcode:
    print(f"failed. the secretcode is {secretcode}")



