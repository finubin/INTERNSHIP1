sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))

attendance = int(input("Enter attendance percentage: "))

if sub1 >= 75 and sub2 >= 75 and attendance >= 80:
    print("Eligible for admission")
else:
    print("Not eligible for admission")