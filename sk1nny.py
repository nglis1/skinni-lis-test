print("sk1nny was here")
from datetime import datetime
current_year = datetime.now().year

name = input("What is your name? ")
age = input("What is your age? ")
number = input("Enter a random number: ")

for i in range(int(number)):
    print(f"{i+1}")
    print(f"Hello {name}! You are {age} years old.")
    year100 = current_year + (100 - int(age))
    print(f"You will turn 100 years old in the year {year100}.\n")
