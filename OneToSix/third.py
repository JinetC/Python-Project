def checkingSpeed(speed):
    if(speed < 70):
        return "OK"
    else:
        speed1 = (speed-70)//5
        if speed1 <= 12:
            return print(f"Point : {speed1}")
        else:
            return print("License suspended")

input_speed = checkingSpeed(int(input("Enter the driver speed : ")))

