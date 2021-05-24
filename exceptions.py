# Original script: https://cs50.harvard.edu/web/2020/notes/2/#exceptions
# Edited by Mossab Diae (github : @mossaybo)
# Added functionality :
#   the program will keep asking for input until a valid input is given
#   if valid x input is already given , it won't ask for it again if an
#   invalid y input is given .

import sys

def getinput(both=True):
    if both:
        try:
            x = None
            x = int(input("x: "))
            y = int(input("y: "))
            return (x, y)
        except ValueError:
            print("Error: Invalid input")
            if x is not None:
                return (x, getinput(both=False))
            else:
                return getinput()
    else:
        try:
            y = int(input("y: "))
            return y
        except ValueError:
            print("Error: Invalid input")
            return getinput(both=False)

x, y = getinput()
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # Exit the program
    sys.exit(1)

print(f"{x} / {y} = {result}")