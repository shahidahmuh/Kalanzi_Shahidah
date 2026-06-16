#Learning how to work with looping through lists

#looping through an entire list 
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(f"{magician.title()}, that was a great trick!")
print(f"{magicians[0].upper()} is not as good as {magicians[-1].upper()} i can assure you." )
