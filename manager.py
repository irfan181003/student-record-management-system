from student import Student


class StudentManager:

    def __init__(self):
        self.students = []

    # Add a student
    def add_student(self, student):
        self.students.append(student)

    # Remove a student using Student ID
    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return True

        return False

    # Search student by ID
    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    # Search students by name
    def search_by_name(self, name):
        results = []

        for student in self.students:
            if student.name.lower() == name.lower():
                results.append(student)

        return results

    # Search students by department
    def search_by_department(self, department):
        results = []

        for student in self.students:
            if student.department.lower() == department.lower():
                results.append(student)

        return results

    # Search students whose average is greater than given value
    def search_by_average(self, minimum_average):
        results = []

        for student in self.students:
            if student.calculate_average() > minimum_average:
                results.append(student)

        return results

    # Display all students
    def display_all_students(self):
        if not self.students:
            print("No students available.")
            return

        for student in self.students:
            student.display_student()
            print("--------------------")

    # Load students from a file
    def load_from_file(self, file_handler, filename, file_format):

        if file_format == "txt":
            self.students = file_handler.read_txt(filename)

        elif file_format == "csv":
            self.students = file_handler.read_csv(filename)

        elif file_format == "json":
            self.students = file_handler.read_json(filename)

        else:
            print("Unsupported file format.")

    # Save students to a file
    def save_to_file(self, file_handler, filename, file_format):

        if file_format == "txt":
            file_handler.write_txt(filename, self.students)

        elif file_format == "csv":
            file_handler.write_csv(filename, self.students)

        elif file_format == "json":
            file_handler.write_json(filename, self.students)

        else:
            print("Unsupported file format.")