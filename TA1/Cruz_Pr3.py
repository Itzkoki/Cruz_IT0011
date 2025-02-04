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