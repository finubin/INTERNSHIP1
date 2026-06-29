mark = float(input("Enter your mark: "))
if mark >= 90:
    print("Grade: A")
elif mark in range(80, 90):
    print("Grade: B")
elif mark in range(70, 80):
    print("Grade: C")
else:
    print("Grade: D")