print(len("my_name"))
print(int(7.9))
print(round(8.88))#Accepts the float value and returns the nearest integer
#Read about the bin() and hex() functions

#Flow Control statements
#Coomparison operators ==, !=, <, >, <=, >=

#if block -if statement could be read as, “If this condition is true, execute the code in the clause.”
name = "Alice"
age = 12
if name == "Alice":
    print("Hi Alice welcome Home!!!")
elif age < 10:
    print("Young Lad")
else :
    print("Not the right Person!!!!")


print('Enter TB or GB for the advertised unit:')
unit = input('>')
# Calculate the amount that the advertised capacity lies:
if unit == 'TB' or unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
    discrepancy = 1000000000 / 1073741824
print('Enter the advertised capacity:')
advertised_capacity = input('>')
advertised_capacity = float(advertised_capacity)
# Calculate the real capacity, round it to the nearest hundredths,
# and convert it to a string so it can be concatenated:
real_capacity = str(round(advertised_capacity * discrepancy, 2))
print('The actual capacity is ' + real_capacity + ' ' + unit)

#Loops 