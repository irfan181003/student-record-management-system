import csv
import json

from student import Student


class FileHandler:

    # =========================
    # TXT FILE HANDLING
    # =========================

    def read_txt(self, filename):

        students = []

        with open(filename, "r") as file:
            lines = file.readlines()

        for line in lines:

            if not line.strip():
                continue

            parts = line.strip().split(",")

            student = Student(
                int(parts[0].strip()),
                parts[1].strip(),
                parts[2].strip(),
                int(parts[3].strip()),
                int(parts[4].strip()),
                int(parts[5].strip()),
                int(parts[6].strip())
            )

            students.append(student)

        return students

    def write_txt(self, filename, students):

        with open(filename, "w") as file:

            for student in students:

                line = (
                    str(student.student_id) + ", " +
                    student.name + ", " +
                    student.department + ", " +
                    str(student.semester) + ", " +
                    str(student.subject1) + ", " +
                    str(student.subject2) + ", " +
                    str(student.subject3) + "\n"
                )

                file.write(line)

    # =========================
    # CSV FILE HANDLING
    # =========================

    def read_csv(self, filename):

        students = []

        with open(filename, "r", newline="") as file:

            reader = csv.reader(file)

            # Skip header
            next(reader)

            for row in reader:

                student = Student(
                    int(row[0]),
                    row[1],
                    row[2],
                    int(row[3]),
                    int(row[4]),
                    int(row[5]),
                    int(row[6])
                )

                students.append(student)

        return students

    def write_csv(self, filename, students):

        with open(filename, "w", newline="") as file:

            writer = csv.writer(file)

            # Write CSV header
            writer.writerow([
                "Student_ID",
                "Name",
                "Department",
                "Semester",
                "Subject1",
                "Subject2",
                "Subject3"
            ])

            # Write student records
            for student in students:

                writer.writerow([
                    student.student_id,
                    student.name,
                    student.department,
                    student.semester,
                    student.subject1,
                    student.subject2,
                    student.subject3
                ])

    # =========================
    # JSON FILE HANDLING
    # =========================

    def read_json(self, filename):

        students = []

        with open(filename, "r") as file:

            data = json.load(file)

        for record in data:

            marks = record["marks"]

            student = Student(
                record["student_id"],
                record["name"],
                record["department"],
                record["semester"],
                marks["subject1"],
                marks["subject2"],
                marks["subject3"]
            )

            students.append(student)

        return students

    def write_json(self, filename, students):

        data = []

        for student in students:

            record = {
                "student_id": student.student_id,
                "name": student.name,
                "department": student.department,
                "semester": student.semester,
                "marks": {
                    "subject1": student.subject1,
                    "subject2": student.subject2,
                    "subject3": student.subject3
                }
            }

            data.append(record)

        with open(filename, "w") as file:

            json.dump(
                data,
                file,
                indent=4
            )