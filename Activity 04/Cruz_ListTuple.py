#Create a record management program given a list of students records.

# Student ID: This must be a six-digit number
# Student Name: Consists of first name and last name (as a tuple)
# Student Class Standing: The student class standing grade
# Major Exam Grade: The student's exam grade

def studentID(student_ID):
    return len(student_ID) == 6 and student_ID.isdigit()

def studentName(name):
    return isinstance(name, tuple) and len(name) == 2 and all(isinstance(n, str) for n in name)

def studentClassGrade(classGrade, examGrade):
    return 0 <= classGrade <= 100 and 0 <= examGrade <= 100

def studentExamGrades(classGrade, examGrade):
    return (classGrade * 0.6) + (examGrade * 0.4)


def main():
    students_Records = []

    def showAllRecords():
        for record in students_Records:
            print(record)

    def orderbyLastName():
        sortedRecords = sorted(students_Records, key=lambda x: x[1][1])
        for record in sortedRecords:
            print(record)

    def orderbyGrade():
        sortedRecords = sorted(students_Records, key=lambda x: studentExamGrades(x[2], x[3]), reverse=True)
        for record in sortedRecords:
            print(record)

    def showStudentRecord():
        student_ID = input("Enter Student ID: ")
        for record in students_Records:
            if record[0] == student_ID:
                print(record)
                return
        print("Student not found")

    def addRecord():
        student_ID = input("Enter Student ID (6 digits): ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        classGrade = float(input("Enter Class Standing Grade: "))
        examGrade = float(input("Enter Major Exam Grade: "))
        name = (first_name, last_name)
        if studentID(student_ID) and studentName(name) and studentClassGrade(classGrade, examGrade):
            record = (student_ID, name, classGrade, examGrade)
            students_Records.append(record)
            print("Record added successfully.")
        else:
            print("Invalid input")

    def editRecord():
        student_ID = input("Enter Student ID to edit: ")
        for i, record in enumerate(students_Records):
            if record[0] == student_ID:
                first_name = input("Enter First Name (press enter to keep current): ") or record[1][0]
                last_name = input("Enter Last Name (press enter to keep current): ") or record[1][1]
                classGrade = input("Enter Class Standing Grade (press enter to keep current): ")
                examGrade = input("Enter Major Exam Grade (press enter to keep current): ")
                classGrade = float(classGrade) if classGrade else record[2]
                examGrade = float(examGrade) if examGrade else record[3]
                name = (first_name, last_name)
                if studentName(name) and studentClassGrade(classGrade, examGrade):
                    students_Records[i] = (student_ID, name, classGrade, examGrade)
                    print("Record updated successfully.")
                else:
                    print("Invalid input")
                return
        print("Student not found")

    def deleteRecord():
        student_ID = input("Enter Student ID to delete: ")
        for i, record in enumerate(students_Records):
            if record[0] == student_ID:
                del students_Records[i]
                print("Record deleted successfully.")
                return
        print("Student not found")

    while True:
        print("\nMenu:")
        print("1. Show All Students Record")
        print("2. Order by Last Name")
        print("3. Order by Grade")
        print("4. Show Student Record")
        print("5. Add Record")
        print("6. Edit Record")
        print("7. Delete Record")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            showAllRecords()
        elif choice == '2':
            orderbyLastName()
        elif choice == '3':
            orderbyGrade()
        elif choice == '4':
            showStudentRecord()
        elif choice == '5':
            addRecord()
        elif choice == '6':
            editRecord()
        elif choice == '7':
            deleteRecord()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
