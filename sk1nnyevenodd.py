num = int(input("Enter a number: "))
divisor = int(input("Enter a divisor: "))
if num % 2 == 0:
    if num % 4 == 0:
        print("The number is even and a multiple of 4.")
    else:
        print("The number is even.")
else:
    print("The number is odd.")

if num % divisor == 0:
    print(f"{num} is divisible by {divisor}.")
else:
    print(f"{num} is not divisible by {divisor}.")