#Output your favourite phone brand
x = ("samsung", "iphone", "tecno", "redmi")
print(x[1])#iPhone

#Print the 2nd last item usng negative indexing
print(x[-1])#redmi

#Update "iphone" to "itel"
phones = list(x)
#phones[1] = "itel"
x = tuple(phones)
print(x)

#Add "Huawei" 
phones = list(x)
#phones.append("Huawei")
x = tuple(phones)
print(x)

#Loop through a tuple
for phone in x:
    print(phone)

#Remove the first item
phones = list(x)
phones.pop(0)
x = tuple(phones)
print(x)

#Create a tuple of cities in Uganda
cities =  tuple(("Kampala", "Jinja", "Mbarara", "Gulu","Mbale"))
print(cities)

#Unpack tuple
city = ("kampala", "mbarara", "jinja")
city1, city2, city3 = city
print(city1)
print(city2)
print(city3)

#print the 2nd, 3rd and 4th cities
print(cities[1:4])

#Join two tuples
first_name = ('Shahidah')
last_name = ("Kalanzi")
full_name = first_name + last_name
print(full_name)

#Multiply tuple of colours by 3
colours = ("red", "blue", "green")
print(colours * 3)

#Count how many times 8 appears
thistuple = ( 1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(8))