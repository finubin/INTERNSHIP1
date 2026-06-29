a = str(input("Enter a character: "))
vowels = "aeiouAEIOU"
count = 0
for char in a:
    if char in vowels:
        count += 1
print("The number of vowels in the character is:", count)