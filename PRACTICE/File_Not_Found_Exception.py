from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} doesnot exist.")
    
    #Analysing text e.g entire books 
    '''
    let us try to count the number of words in the text.
    THIS CAN ALSO BE USED IF YOU WANT TO WORK WITH LITERATURE WORKS.
    '''
else:
    #Count the approximate number of words in the file 
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

#WORKING WITH MULTIPLE FILES
#add a count_words(path) function and  count_words(path)
'''
def count_words(path): count the approximate number of words in a file

try......

path = Path('alice.txt)
count_words(path)

'''

''' 
FAILING SILENTLY

try:
----snip----
except fileNotFoundError:
    pass
else:
----snip----    

'''