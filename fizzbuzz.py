# Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.



int1 = int(input("Enter a number "))
if ((int1 % 3 == 0) & (int1 % 5 != 0)):
    print("Fizz")
if (int1 % 5 == 0) & (int1 % 3 != 0):
    print("Buzz")
if ((int1 % 3== 0) & (int1 % 5 == 0)):
    print("FizzBuzz")
if ((int1 % 3 != 0) & (int1 % 5 != 0)):
    print(int1)