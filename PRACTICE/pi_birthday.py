from pathlib import Path
path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input('Enter your birthday, in the form of mmddyy: ')
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!!")
else:
    print("Your Birthday doesnot appear in the first million digits of pi.")

print(f'{pi_string[:52]}...')
print (len(pi_string))
