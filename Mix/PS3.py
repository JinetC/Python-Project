num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))


def smaller_number(num1, num2):
    if num1 >= num2:
        return num2
    else:
        return num1


smaller_number(num1,num2)
print("Smallest number is:",smaller_number(num1,num2))