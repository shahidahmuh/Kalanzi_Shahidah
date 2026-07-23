#Using the json.dumps() function -- this takes one argument i.e. a piece of data that is to be converted to JSON format

from pathlib import Path
import json

'''numbers = [2, 3, 4, 5, 10]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)

'''

# A program that uses the json.loads() function 
'''
from pathlib import Path 
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
'''

#Saving and Reading User Generated Data 


#Storing user input 
'''
username = input('What is your name?')
path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f'We will remember you , {username}!!')

'''

#a program that greets a user whose nam has been stored already 
'''
path = Path('username.json)
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}")

'''

#Combining both programs
path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Wecome back, {username}")

else:
    username = input("What is your name?")
    contents =json.dumps(username)
    path.write_text(contents)
    print(f'We will remember you , {username}!!')


#REFACTORING == breaking the code into a series of functions that have specific jobs







