# 3.3. Practical Problem Solving with String Manipulation and File Handling
lastname = input("Enter your last name: ")
firstname = input("Enter your first name: ")
age = input("Enter age: ")
contact = input("Enter contact number: ")
course = input("Enter course: ")

studentinfo = "Last Name: " + lastname + "\n" + "First Name: " + firstname + "\n" + "Age: " + age + "\n" + "Contact Number: " + contact + "\n" + "Course: " + course + "\n" + " " + "\n"

with open("students.txt", "a") as f:
    f.write(studentinfo)

print("Student information has been saved to 'students.txt'.")
