score1 = float(input("Enter score of student 1: "))
score2 = float(input("Enter score of student 2: "))
score3 = float(input("Enter score of student 3: "))
score4 = float(input("Enter score of student 4: "))

if score1 >= score2 and score1 >= score3 and score1 >= score4:
    print("The highest score is:", score1)
elif score2 >= score1 and score2 >= score3 and score2 >= score4:
    print("The highest score is:", score2)
elif score3 >= score1 and score3 >= score2 and score3 >= score4:
    print("The highest score is:", score3)
else:
    print("The highest score is:", score4)