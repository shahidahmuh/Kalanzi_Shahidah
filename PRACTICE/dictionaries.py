
myCat = {'size':'fat', 'age':17, 'type': 'Germany'}
#Access pthe values using their keys 
print(f"My cat is a " +myCat['type'] )

#dictionaries can also store integers as keys e.g
spam ={12:'win win!!', 10: 'free spin'}
spam.setdefault(1,'black')#Setting a default value

for v in spam.values():#Returning values in the dictionary
    print(v)
for k in spam.keys():#Returning all the keys in the dictionary
    print(k)
print(spam[12])

#EXAMPLE : Birthdays
 
'''birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')'''

