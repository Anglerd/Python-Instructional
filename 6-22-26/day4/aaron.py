class Student:
    next_id = 1
 
    def __init__(self, name, sex, grade):
        self.id = Student.next_id
        Student.next_id += 1
 
        self.name = name
        self.sex = sex
        self.grade = grade
 
    def display(self):
        print("----------------------------")
        print(f"ID    : {self.id}")
        print(f"Name  : {self.name}")
        print(f"Sex   : {self.sex}")
        print(f"Grade : {self.grade}")
        print(f"Letter: {self.letter_grade()}")
 
    def letter_grade(self):
        if self.grade >= 90:
            return "A"
        elif self.grade >= 80:
            return "B"
        elif self.grade >= 70:
            return "C"
        elif self.grade >= 60:
            return "D"
        else:
            return "F"
 
 
students = []
 
 
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
 
 
def add_student():
    name = input("Student Name: ").strip()
    sex = input("Sex (M/F): ").strip().upper()
 
    grade = get_number("Grade: ")
 
    student = Student(name, sex, grade)
    students.append(student)
 
    print("Student added!")
 
 
def view_students():
    if len(students) == 0:
        print("No students found.")
        return
 
    for student in students:
        student.display()

 
def search_student():
    search = input("Enter ID: ").strip().lower()
 
    if student[search]:
        return student
 
    if not found:
        print("Student not found.")


def display_single_student(student):
    student = search_student()
    if not student:
        return
    student.display()


def update_grade():
    student = search_student()
    if not student:
        return
    new_grade = get_number("New Grade: ")
    student.grade = new_grade
    print("Grade updated!")
    return
 
 
def remove_student():
    student = search_student()
    if not student:
        return
    students.remove(student)
    print("Student removed.")
    return
 
 
def highest_grade():
    if len(students) == 0:
        print("No students found.")
        return
 
    #max = 0
    #for student in students:
    #    if student.grade > max:
    #        max = student.grade
    #        top_student = student
    
    top_student = max(students, key=lambda student: student.grade)
 
    print("Highest Grade:")
    top_student.display()
 
 
def average_grade():
    if len(students) == 0:
        print("No students found.")
        return
 
    total = 0
 
    for student in students:
        total += student.grade
 
    average = total / len(students)
 
    print(f"Class Average: {average:.2f}")
 
 
def sort_students():
    if len(students) == 0:
        print("No students found.")
        return
 
    print("""
Sort By:
1. Name A-Z
2. Name Z-A
3. Grade Low to High
4. Grade High to Low
""")
 
    choice = input("Choose sort option: ")
 
    if choice == "1":
        sorted_students = sorted(students, key=lambda student: student.name.lower())
    elif choice == "2":
        sorted_students = sorted(students, key=lambda student: student.name.lower(), reverse=True)
    elif choice == "3":
        sorted_students = sorted(students, key=lambda student: student.grade)
    elif choice == "4":
        sorted_students = sorted(students, key=lambda student: student.grade, reverse=True)
    else:
        print("Invalid option.")
        return
 
    for student in sorted_students:
        student.display()
 
 
def save_students():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(f"{student.id},{student.name},{student.sex},{student.grade}\n")
 
    print("Students saved to students.txt")
 
 
def load_students():
    students.clear()
 
    try:
        with open("students.txt", "r") as file:
            highest_id = 0
 
            for line in file:
                student_id, name, sex, grade = line.strip().split(",")
 
                student = Student(name, sex, float(grade))
                student.id = int(student_id)
 
                students.append(student)
 
                if student.id > highest_id:
                    highest_id = student.id
 
            Student.next_id = highest_id + 1
 
        print("Students loaded.")
 
    except FileNotFoundError:
        print("No save file found yet.")
 
    except ValueError:
        print("Save file is damaged or formatted incorrectly.")
       
def load_test_data():
        students.clear()
        Student.next_id = 1
 
        test_students = [
        ("Aaron", "M", 100),
        ("Jane", "F", 88),
        ("Michael", "M", 72),
        ("Sarah", "F", 91),
        ("Chris", "M", 65),
        ("Emily", "F", 84),
        ("David", "M", 77),
        ("Jessica", "F", 99),
        ("Brian", "M", 58),
        ("Ashley", "F", 81)
    ]
 
        for name, sex, grade in test_students:
            students.append(Student(name, sex, grade))
 
        print(f"{len(students)} test students loaded successfully!")
 
def main():
    while True:
        print("""
========== Student Database ==========
 
1. Add Student
2. View Students
3. Search Student
4. Update Grade
5. Remove Student
6. Show Highest Grade
7. Show Average Grade
8. Sort Students
9. Save to File
10. Load from File
11. Load Test Data
0. Exit
""")
 
        choice = input("Select Option: ")
 
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_grade()
        elif choice == "5":
            remove_student()
        elif choice == "6":
            highest_grade()
        elif choice == "7":
            average_grade()
        elif choice == "8":
            sort_students()
        elif choice == "9":
            save_students()
        elif choice == "10":
            load_students()
        elif choice == "11":
            load_test_data()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")
 
 
if __name__ == "__main__":
    main()