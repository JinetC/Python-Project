# print('Hello World')
import re
userInput = input("Input your password here")
x = True
while x:
    if (len(userInput) < 6 or len(userInput) > 16):
        break
    elif not re.search("[a-z]", userInput):
        break
    elif not re.search("[A-Z]", userInput):
        break
    elif not re.search("[0-9]", userInput):
        break
    elif not re.search("[$#@]", userInput):
        break
    elif re.search("\s", userInput):
        break
    else:
        print("Valid Password")
        x = False
        break
if x:
    print("Not a Valid Password")