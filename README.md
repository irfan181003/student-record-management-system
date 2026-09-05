# Student Record Management & Search System

## Objective

The objective of this project is to develop a Student Record Management
and Search System using Python and Object-Oriented Programming.

The system stores student information and provides operations such as
adding, removing, displaying, searching, updating marks and calculating
student results.

## Features

- Add student records
- Remove student records
- Display all students
- Search by Student ID
- Search by Name
- Search by Department
- Search by Average
- Calculate total marks
- Calculate average marks
- Determine Pass/Fail result
- Update student marks
- Read TXT files
- Read and write CSV files
- Read and write JSON files
- Save updated records
- Command-line arguments using argparse

## Project Structure

student-record-system/

    main.py
    student.py
    manager.py
    file_handler.py

    data/
        students.txt
        students.csv
        students.json

## Requirements

- Python 3.x
- Built-in csv module
- Built-in json module
- Built-in argparse module

No Pandas or NumPy libraries are used.

## Object-Oriented Programming

The project uses two main classes.

### Student

The Student class stores:

- Student ID
- Name
- Department
- Semester
- Subject 1 marks
- Subject 2 marks
- Subject 3 marks

Methods include:

- calculate_total()
- calculate_average()
- get_result()
- display_student()
- update_marks()

### StudentManager

The StudentManager class manages multiple Student objects.

Methods include:

- add_student()
- remove_student()
- search_student()
- search_by_name()
- search_by_department()
- search_by_average()
- display_all_students()
- load_from_file()
- save_to_file()

## File Handling

The system supports three file formats.

### TXT

The TXT file contains comma-separated student records.

### CSV

The CSV file contains a header and student records.
Python's csv module is used to read and write CSV files.

### JSON

The JSON file stores student information as a list of dictionaries.
Python's json module is used to read and write JSON files.

## How to Run

For TXT:

python main.py --file data/students.txt --format txt --output data/students_updated.txt

For CSV:

python main.py --file data/students.csv --format csv --output data/students_updated.csv

For JSON:

python main.py --file data/students.json --format json --output data/students_updated.json

## Searching

The system uses basic Python loops and conditions for searching.

Students can be searched by:

- Student ID
- Name
- Department
- Average marks

## Testing

The system was tested using at least five student records.

The following operations were tested:

- Displaying students
- Searching by ID
- Searching by name
- Searching by department
- Searching by average
- Adding a student
- Removing a student
- Updating marks
- Saving records

## Conclusion

The Student Record Management and Search System demonstrates the use of
Object-Oriented Programming, file handling, searching, command-line
arguments and Python built-in modules.

The project successfully manages student records using TXT, CSV and
JSON files.