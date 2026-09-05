class Student:

    def __init__(self, student_id, name, department, semester,
                 subject1, subject2, subject3):

        self.student_id = student_id
        self.name = name
        self.department = department
        self.semester = semester
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3

    # Calculate total marks
    def calculate_total(self):
        return self.subject1 + self.subject2 + self.subject3

    # Calculate average marks
    def calculate_average(self):
        total = self.calculate_total()
        return total / 3

    # Check pass or fail
    def get_result(self):
        if (self.subject1 >= 40 and
                self.subject2 >= 40 and
                self.subject3 >= 40):
            return "Pass"
        else:
            return "Fail"

    # Display complete student information
    def display_student(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Semester:", self.semester)
        print("Subject 1:", self.subject1)
        print("Subject 2:", self.subject2)
        print("Subject 3:", self.subject3)
        print("Total:", self.calculate_total())
        print("Average:", round(self.calculate_average(), 2))
        print("Result:", self.get_result())

    # Update student marks
    def update_marks(self, subject1, subject2, subject3):
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3