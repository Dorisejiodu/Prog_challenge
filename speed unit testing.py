def driver_speed(speed):
    speed = int(input("Enter your speed  "))
    if speed < 70:
        print("OK")
    else:
        point_formular = (speed - 70)//5
        if point_formular <= 12:
            print ("point:", point_formular)
        else:
            print ("Licence suspended")


#x = driver_speed(90)
#print(x)
