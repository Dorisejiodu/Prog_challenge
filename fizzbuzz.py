# Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.

def fizz_buzz(int1):
    int1 = int(input("Enter a number "))
    if ((int1 % 3 == 0) & (int1 % 5 != 0)):
        return "Fizz"
    if (int1 % 5 == 0) & (int1 % 3 != 0):
        return "Buzz"
    if ((int1 % 3== 0) & (int1 % 5 == 0)):
        return "FizzBuzz"
    if ((int1 % 3 != 0) & (int1 % 5 != 0)):
        return int1

int1 = fizz_buzz(15)
print(int1)

int1 = fizz_buzz(6)
print(int1)

int1 = fizz_buzz(10)
print(int1)

int1 = fizz_buzz(22)
print(int1)