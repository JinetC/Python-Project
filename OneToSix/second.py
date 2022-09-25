temp = input("Input the temperature you like to convert? (like: 45F, 102C etc.) : ")
degree = int(temp[:-1])
val1 = temp[-1]

if val1.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  convert = "Fahrenheit"
elif val1.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  convert = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", convert, "is", result, "degrees.")