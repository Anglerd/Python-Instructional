list_of_nums = [1, 2, 3]
list_of_string = list("asd")
list_of_list = [{}]

dictionary = {"key1": "value1", "key2": 2, "key3": [1, 2], "key4": {"key1_1": "value1"}} # {}

"""
for num in list_of_nums:
    print(num)
"""

# print(dictionary)
#for key in dictionary:
#    print(dictionary[key])

list_of_nums[0] == 1
dictionary["key1"] == "value1"
dictionary["key2"] == 2

#for value in dictionary.values():
#    print(value)

#for key, value in dictionary.items():
#    print(f"key: {key}, value: {value}")

"""
class Student:
    def __init__(self, name: str, age: int, school_level: int, gender: str, email: str, student_id: int):
        self.name = name
        self.age = age
        self.school_level = school_level
        self.gender = gender
        self.email = email
        self.student_id = student_id
        self.balance = 0.0
"""

def add_student(name, age, school_level, gender, email, student_id) -> dict:
    add_student = {
        "name": name,
        "age": age,
        "school_level": school_level,
        "gender": gender,
        "email": email,
        "student_id": student_id,
        "balance": 0.0
        }
    return add_student

#print(students)

#f"This is {self.name}, a {self.age}-year-old {self.gender} student in grade {self.school_level}. You can reach them at {self.email}. Their student ID is {self.student_id}"

def pretty_print_students(students: list):
    for student in students:
        print(f"This is {student["name"]}, a {student["age"]}-year-old {student["gender"]} student in grade {student["school_level"]}. You can reach them at {student["email"]}. Their student ID is {student["student_id"]}")

def get_input(prompt: str, type_converter):
    """This function will prompt the user for some input, and convert it using the type_converter type"""
    while True:
        try:
            return type_converter(input(prompt))
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    student_id = 0
    students = []
    while True:
        student_id += 1
        name = input("Please enter your name ")
        age = get_input("Enter your age ", int)
        school_level = get_input("School level in grade years. Ex. 12 ", int)
        gender = input("Gender")
        email = input("Email")
        students.append(add_student(name, age, school_level, gender, email, student_id))
        if "y" not in input("Would you like to continue? y/n").lower():
            break
    pretty_print_students(students)