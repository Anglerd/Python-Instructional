# import large_database_file
# python is an object oriented programming language. What does that mean?

class Student:
    def __init__(self, name, sex, grade):
        self.name = name
        self.sex = sex
        self.grade = grade
    
    def new_grade(self, new_grade):
        self.grade = (self.grade + new_grade) / 2

    def sex_change(self, new_sex):
        self.sex = new_sex
    
    def new_name(self, new_name):
        self.name = new_name

    def __str__(self):
        return f"Student: {self.name}, Sex: {self.sex}, Grade: {self.grade}"

class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students

    #def print_students(self):
    #    group_of_students = ""
    #    for student_id in self.students:
    #        this_student = self.students[student_id]
    #        group_of_students += f"Student ID: {student_id}, Name: {this_student.name}, Sex: {this_student.sex}, Grade: {this_student.grade}"
    #    return group_of_students

    def __str__(self):
        group_of_students = ""
        for student_id in self.students:
            this_student = self.students[student_id]
            group_of_students += this_student.__str__()
        return f"School: {self.name}, Students: {group_of_students}"

if __name__ == "__main__":
    # database_file = load(large_database_file)
    local_copy_of_database_file = { 1: Student("Jody", "M", 10), 2: Student("Jane", "F", 11) }
    # database_file = { 1: Student("name": "Jody", "sex": "M", "grade": 10}, 2: {"name": "Jane", "sex": "F", "grade": 11}}
    # student1 = Student("Jody", "M", 10)
    # student2 = Student("Jane", "F", 11)

    # print(f"Student 1: {student1.name}, Sex: {student1.sex}, Grade: {student1.grade}")
    # print(f"Student 2: {student2.name}, Sex: {student2.sex}, Grade: {student2.grade}")

    # student1.new_grade(12)
    print(f"Student 1: {local_copy_of_database_file[1].name}, Sex: {local_copy_of_database_file[1].sex}, Grade: {local_copy_of_database_file[1].grade}")

    local_copy_of_database_file[1].sex_change("F")
    # local_copy_of_database_file[1]["sex"] = "F" # this is what you would use if we didn't have the protected write for the class

    print(f"Student 1: {local_copy_of_database_file[1].name}, Sex: {local_copy_of_database_file[1].sex}, Grade: {local_copy_of_database_file[1].grade}")

    my_school = School("My School", local_copy_of_database_file)

    # print(f"School Name: {my_school.name}, Students: {my_school.print_students}")
    print(my_school)

    # save(large_database_file, database_file)
    student_name = input("Enter student name: ")
    student_sex = input("Enter student sex: ")
    student_grade = int(input("Enter student grade: "))

    student1 = Student(student_name, student_sex, student_grade)

    # student2 = Student(input("Enter student name: "), input("Enter student sex: "), int(input("Enter student grade: ")))

    print(f"Student 1: {student1.name}, Sex: {student1.sex}, Grade: {student1.grade}")
    # print(f"Student 2: {student2.name}, Sex: {student2.sex}, Grade: {student2.grade}")
    student1.new_grade(13)
    # student2.new_grade("13")
    print(f"Student 1: {student1.name}, Sex: {student1.sex}, Grade: {student1.grade}")
    # print(f"Student 2: {student2.name}, Sex: {student2.sex}, Grade: {student2.grade}")

    while true:
        try:
            input(something)
            something
            break
        except (some error):
            print("stop being mean to me")