# **** input returns a string; we need an integer value ****
num = int(input(">>> please enter a number: "))

# **** heart character (unicode) ****
heart_char = '❤'

# **** num must be an integer not a string ****
for i in range(num):
    print(heart_char + " ", end='')
print()

# **** print * num ****
heart_str = heart_char + " "
print(heart_str * 5, end='')
print()

# **** list comprehension ****
hearts = ['❤' for i in range(num)]

# **** unpack list and print elements ****
print(*hearts, sep = ' ')

# **** display hearts ****
print(' '.join(hearts))
print()
