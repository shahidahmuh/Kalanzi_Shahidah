import this 
message = "\n\nHello Python World"
print(message)
message= "hi people" 
print(message)

name = "ada lovelace"
print(name.title()) 

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name) 

#using a variables value inside a string
print(f"Hello, {last_name}\t {first_name}\n this is a greeting from the team!")
print(f"look through this {full_name.upper()}")

message = f"THIS IS NEW {full_name.lower()}"
print(message)

x=10
y=6
# write the constants in capital letters since python has no built in definition for constants
CONSTANT = 10000
a,b,c = 10, 12, 13
z= 14_000_000_000
print((x**y)+x**2)
print(z)

message= f"hello Uganda {z}"
print(message)
