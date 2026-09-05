import argparse

from student import Student
from manager import StudentManager
from file_handler import FileHandler


# ==========================================
# COMMAND LINE ARGUMENTS
# ==========================================

def create_parser():

    parser = argparse.ArgumentParser(
        description="Student Record Management and Search System"
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Path of the student data file"
    )

    parser.add_argument(
        "--format",
        required=True,
        choices=["txt", "csv", "json"],
        help="Format of the student data file"
    )

    parser.add_argument(
        "--output",
        required=False,
        help="Path of the output file"
    )

    return parser


# ==========================================
# MENU
# ==========================================

def show_menu():

    print()
    print("========================================")
    print(" Student Record Management System")
    print("========================================")
    print("1. Display all students")
    print("2. Search by Student ID")
    print("3. Search by Name")
    print("4. Search by Department")
    print("5. Search by Average")
    print("6. Add a student")
    print("7. Remove a student")
    print("8. Update student marks")
    print("9. Save students")
    print("10. Exit")


# ==========================================
# ADD STUDENT
# ==========================================

def add_student(manager):

    print("\nEnter student details")

    student_id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    semester = int(input("Enter Semester: "))

    subject1 = int(input("Enter Subject 1 marks: "))
    subject2 = int(input("Enter Subject 2 marks: "))
    subject3 = int(input("Enter Subject 3 marks: "))

    new_student = Student(
        student_id,
        name,
        department,
        semester,
        subject1,
        subject2,
        subject3
    )

    manager.add_student(new_student)

    print("Student added successfully.")


# ==========================================
# SEARCH BY ID
# ==========================================

def search_by_id(manager):

    student_id = int(input("Enter Student ID: "))

    student = manager.search_student(student_id)

    if student:
        student.display_student()
    else:
        print("Student not found.")


# ==========================================
# SEARCH BY NAME
# ==========================================

def search_by_name(manager):

    name = input("Enter student name: ")

    results = manager.search_by_name(name)

    if results:

        for student in results:
            student.display_student()
            print("--------------------")

    else:
        print("No students found.")


# ==========================================
# SEARCH BY DEPARTMENT
# ==========================================

def search_by_department(manager):

    department = input("Enter department: ")

    results = manager.search_by_department(department)

    if results:

        for student in results:
            student.display_student()
            print("--------------------")

    else:
        print("No students found.")


# ==========================================
# SEARCH BY AVERAGE
# ==========================================

def search_by_average(manager):

    minimum_average = float(
        input("Enter minimum average: ")
    )

    results = manager.search_by_average(
        minimum_average
    )

    if results:

        for student in results:
            student.display_student()
            print("--------------------")

    else:
        print("No students found.")


# ==========================================
# REMOVE STUDENT
# ==========================================

def remove_student(manager):

    student_id = int(
        input("Enter Student ID to remove: ")
    )

    removed = manager.remove_student(student_id)

    if removed:
        print("Student removed successfully.")
    else:
        print("Student not found.")


# ==========================================
# UPDATE MARKS
# ==========================================

def update_student_marks(manager):

    student_id = int(
        input("Enter Student ID: ")
    )

    student = manager.search_student(student_id)

    if student:

        print("Enter new marks")

        subject1 = int(
            input("Enter Subject 1 marks: ")
        )

        subject2 = int(
            input("Enter Subject 2 marks: ")
        )

        subject3 = int(
            input("Enter Subject 3 marks: ")
        )

        student.update_marks(
            subject1,
            subject2,
            subject3
        )

        print("Student marks updated successfully.")

    else:
        print("Student not found.")


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    parser = create_parser()

    args = parser.parse_args()

    file_handler = FileHandler()

    manager = StudentManager()

    # Load data from selected file
    manager.load_from_file(
        file_handler,
        args.file,
        args.format
    )

    print()
    print("Students loaded successfully.")
    print("Total students:", len(manager.students))

    # Menu loop
    while True:

        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":

            manager.display_all_students()

        elif choice == "2":

            search_by_id(manager)

        elif choice == "3":

            search_by_name(manager)

        elif choice == "4":

            search_by_department(manager)

        elif choice == "5":

            search_by_average(manager)

        elif choice == "6":

            add_student(manager)

        elif choice == "7":

            remove_student(manager)

        elif choice == "8":

            update_student_marks(manager)

        elif choice == "9":

            if args.output:

                manager.save_to_file(
                    file_handler,
                    args.output,
                    args.format
                )

                print(
                    "Students saved successfully to:",
                    args.output
                )

            else:

                print(
                    "No output file specified."
                )

                print(
                    "Use --output to specify the output file."
                )

        elif choice == "10":

            print(
                "Thank you for using the Student "
                "Record Management System."
            )

            break

        else:

            print(
                "Invalid choice. Please try again."
            )


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":
    main()