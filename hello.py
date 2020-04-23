import re

# **** ****
print('<<< Hello world!')
print("<<< Hello world!")
print()

# **** single or double quotes ****
name = input(">>> name: ")
print("<<< Hello", name)
print('<<< Hello ' + name)
print()

# **** check if name is capitalized ****
if name.capitalize() == 'John':
    print("<<< Hello " + name + " - true")
else:
    print("<<< Hello " + name + " - false")
print()

# **** extract and display first and last names ****
names = name.split()
if len(names) >= 1:
    print("<<< firstName: " + names[0].capitalize())
else:
    print("<<< first name not specified")

if len(names) >= 2:
    print("<<<  lastName: " + names[-1].capitalize())
else:
    print("<<< last name not specified")
print()

# **** ****
if names[0].lower() == 'john' and names[-1].lower() == 'canessa':
    print("<<< " + name.lower().title())
else:
    print("<<< " + names[0].capitalize() + " " + names[-1].capitalize())
print()

# **** ****
print("<<< name ==>" + name + "<==")
print()

# **** using search instead of match ****
if re.search(r'^John\s+(.+\s+)*Canessa$', name, re.IGNORECASE):
    print("<<< " + name.title() + " - true")
else:
    print("<<< " + name.title() + " - false")