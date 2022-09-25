never = float(input("Enter the non-vaccinate people:"))
ones = float(input("Enter one time vaccinate people:"))
twice = float(input("Enter two times vaccinate people:"))
thrice = float(input("Enter three times vaccinate people:"))


def get_mean(never, ones, twice, thrice):
    count = never + ones + twice + thrice
    total = 0 * never + 1 * ones + 2 * twice + 3 * thrice
    mean = total / count
    return mean


print(get_mean(never,ones, twice, thrice))