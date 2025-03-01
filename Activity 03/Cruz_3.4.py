# 3.4 Activity for Reading File Contents and Display
try:
    with open("Activity 03/students.txt", "r") as f:
        content = f.read()
        if content:
            print("Reading Student Information:")
            print(content)
        else:
            print("No student information found.")
except FileNotFoundError:
    print("The file 'students.txt' does not exist.")
