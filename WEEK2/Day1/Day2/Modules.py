#Modules help organise code into reusable
#both inbuilt and external 
#Inbuilt can be accessed using the import keyword

#Using the math module - inbuilt
import math
pie = math.pi
print("Value of pi:", pie)

#steps of using external modules
#1- Install the module first using pip install module_name
#examples of external modules i.e pandas, numpy, scipy e.t.c

import pandas
#Create a simple dataframe

data = {
    "Name": ["John","Agnes","Peter"],
    "Age":[21, 23, 20]

}
print(data)
#Converting the dictionary into a data frame
df = pandas.DataFrame(data)
print(df)

#importing specific functions: this makes the code cleaner and avoids unnecessary imports
from math import pi
print(pi)

#Importing modules with Aliases 
#use the as keyword 
import math as m
result = m.sqrt(16)
print("Square root of 16:", result)

#Importing everything dfrom a module
#from math import *
#print (pi)

#print (factorial(8))

#Add __init__.py in the folder to make it a library