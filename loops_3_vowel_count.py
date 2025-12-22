str = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in str:
    if char in vowels:
        count += 1 

print("Number of vowels in the string:", count)