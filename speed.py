# Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit 
# point and print the total number of demerit points. For example, if the speed is 80, 
# it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended"

def driver_speed(speed):
    speed = int(input("Enter your speed  "))
    if speed < 70:
        return "OK"
    else:
        point_formular = (speed - 70)//5
        if point_formular <= 12:
            return "point:",  point_formular
        else:
            return "Licence suspended"

speed = driver_speed(80)
print(speed)
