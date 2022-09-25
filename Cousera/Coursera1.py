score = input("Enter Score: ")
isc = float(score)
if 0 <= isc < 0.6:
    print("F")
elif 0.6 <= isc < 0.7:
    print("D")
elif 0.7 <= isc < 0.8:
    print("C")
elif 0.8 <= isc < 0.9:
    print("B")
elif 0.9 <= isc <= 1:
    print("A")
else:
    print("error")
