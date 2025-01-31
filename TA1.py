#Count vowels and consonat

count_vowels = 0
count_consonant = 0

print("\nCount vowels and consonat")
variable = input("Enter a string here:")
vowels = "AEIOUaeiou"

for x in variable:
    if x in vowels:
        count_vowels += 1
    else:
        count_consonant += 1
        
print("Vowels count:",count_vowels)
print("Consonant count:",count_consonant)


#Sum of all Digits in a String

print("\nSum of all Digits in a String")
s = input("Enter: ")
sum = 0

for i in s:
    if i.isdigit():
        sum += int(i)    
print("Sum: ",sum)