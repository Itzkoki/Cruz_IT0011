#3.1. Activity for Performing String Manipulations
firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
age = input("Enter your age: ")

fullname = firstname + " " + lastname

print("\nFull Name: ", fullname)
print("Sliced Name: ", firstname[:4])
print("Greeting Message: Hello, " + firstname[:4] + "! Welcome. You are " + age + " years old.")


