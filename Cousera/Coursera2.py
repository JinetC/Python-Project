def computepay(hrs, r):
    x = hrs * r
    if hrs > 40:
        y = (hrs - 40) * (r / 2)
        total = x + y
        return total
    else:
        return x


hrs = float(input("Enter Hours:"))
r = float(input("Enter rates per hour:"))
p = computepay(hrs,r)
print("Pay", p)
