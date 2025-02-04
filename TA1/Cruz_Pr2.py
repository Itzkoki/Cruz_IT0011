#2.) Sum of all Digits in a String
print("\nSum of all Digits in a String")
s = input("Enter String and Digits: ")
sum = 0

for i in s:
    sum += int(i)
print("The total sum is: ", sum)