day = int(input("Enter a day number (1-7): "))
if day in [1, 2, 3, 4, 5]:
    print("It's a weekday.")
elif day in [6, 7]:
    print("It's a weekend.")
else:
    print("Invalid day number. Please enter a number between 1 and 7.")