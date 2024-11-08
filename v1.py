students = []

# Function to add a new student
def add_student(id, name, age, grade):
    student = {
        "ID": id,
        "Name": name,
        "Age": age,
        "Grade": grade
    }
    students.append(student)
    print(f"Student {name} added successfully.")

# Function to delete a student by ID
def delete_student(id):
    global students
    students = [student for student in students if student["ID"] != id]
    print(f"Student with ID {id} deleted successfully.")

# Function to search for a student by ID
def search_student(id):
    for student in students:
        if student["ID"] == id:
            print("Student found:", student)
            return student
    print("Student not found.")
    return None

# Function to update a student record by ID
def update_student(id, name=None, age=None, grade=None):
    for student in students:
        if student["ID"] == id:
            if name:
                student["Name"] = name
            if age:
                student["Age"] = age
            if grade:
                student["Grade"] = grade
            print(f"Student with ID {id} updated successfully.")
            return
    print("Student not found.")

# Function to sort students by a specified key (ID, Name, Age, Grade)
def sort_students(by="ID"):
    if by in ["ID", "Name", "Age", "Grade"]:
        sorted_list = sorted(students, key=lambda x: x[by])
        display_students(sorted_list)
    else:
        print("Invalid sort key.")

# Function to display all students
def display_students(student_list=None):
    if student_list is None:
        student_list = students
    if not student_list:
        print("No students to display.")
    else:
        print("Student Records:")
        for student in student_list:
            print(student)

# Sample usage
add_student(1, "Aditya", 20, "A")
add_student(2, "Mokshit", 22, "B")
display_students()

search_student(1)

update_student(1, age=21)
display_students()

delete_student(2)
display_students()

sort_students(by="Name")
