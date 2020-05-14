cache = {}
def fib(n):
    if n in cache:
        return cache[n]
    
    # Base cases
    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    # Recursion step
    elif n > 1:
        value = fib(n-1) + fib(n-2)

    cache[n] = value
    return value

while(True):
    value = int(input("Enter number to test fib: "))

    while(True):
        if value < 0:
            value = int(input("Please enter a number greater than or equal to 0: "))
        if type(value) != int:
            #value = int(input("Please enter an integer: "))
            raise ValueError("Please enter an integer!")
        if value >= 0:
            break

    for i in range(0, value+1):
        print( str(i) + ": " + str( fib(i) ) )

    loop = input("Want to try again? [y/n] ")

    while(True):
        if loop == "y":
            continue
        elif loop == "n":
            print("Goodbye!")
            break
        else:
            print("Invalid input")
            loop = input("Want to try again? [y/n] ")
    break

exit(1)

