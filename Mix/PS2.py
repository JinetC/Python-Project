num1 = int(input("enter the number 1:"))
num2 = int(input("enter the number 2:"))
num3 = int(input("enter the number 3:"))


def number(num1, num2, num3):
    d = num1 * num2 * num3
    f = d * 2
    return f


print("The product is", number(num1, num2, num3))
