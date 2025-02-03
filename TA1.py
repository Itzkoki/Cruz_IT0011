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


#2.) Sum of all Digits in a String
print("\nSum of all Digits in a String")
s = input("Enter String and Digits: ")
sum = 0

for i in s:
    sum += int(i)
print("The total sum is: ", sum)


#3. A. Nested Loop 
print("\nProgram A Nested For statement")
n = (int(input("Enter your number: ")))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()
   
    
#3. B. While Loop
print("\nProgram B Nested While statement")
n = int(input("Enter any number: "))
row = 1

while row <= n:
    print(str(row) * row)
    row += 1
