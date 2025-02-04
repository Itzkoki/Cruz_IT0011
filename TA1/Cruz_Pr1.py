#1.) Count Vowels and Consonat
count_vowels = 0
count_consonant = 0

print("\nCount Vowels and Consonat")
variable = input("Enter a String here: ")
vowels = "AEIOUaeiou"

for x in variable:
    if x in vowels:
        count_vowels += 1
    else:
        count_consonant += 1
        
print("Vowels count: ",count_vowels)
print("Consonant count: ",count_consonant)