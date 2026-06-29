num = int(input("Enter a number: "))
for i in range(50, 101):
    if num == i:
        print(f"{num} lies between 50 and 100.")
        break
else:
    print(f"{num} does not lie between 50 and 100.")