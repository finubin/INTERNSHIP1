age = int(input("Enter your age: "))
if age<=13:
    print("child.")
elif age in range(13,20):
    print("teenager.")
elif age in range(20,60):
    print("adult.")  
else:    
    print("senior citizen.")