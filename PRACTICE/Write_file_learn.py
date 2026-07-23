from pathlib import Path 
contents = "I love programming\n"
contents += "I love creating new games\n"
contents += "I love Ai and data\n"
contents += "I love everything\n"

path = Path('programming.txt')
path .write_text(contents)
print("content written!")
#path.write_text("I love Programming")