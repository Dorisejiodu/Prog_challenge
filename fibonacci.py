def fibonacci(n):
    """Return the nth number in the Fibonacci sequence"""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else: 
        return(fibonacci(n - 1)) + (fibonacci(n - 2))
n= fibonacci(3)
print(n)
