char = str(input("Enter a character: "))
count = 0
for c in char:
    if c in 'aeiouAEIOU':
        count += 1
print("Number of vowels in the string:", count)