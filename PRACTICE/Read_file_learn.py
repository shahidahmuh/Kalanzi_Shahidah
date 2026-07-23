from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip() #Removing the extra blank line 

#contents = path.read_text().rstrip()
'''
Read returns an empty string when it reaches the end of the file thus showing up as ablank space
this is the only difference between the output and the original file

'''

#Accessing a files lines 
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string)) 
print(contents)

#print(Path.cwd())

