print("Today we will get lots of input from the user and store it in a variable")
print("We will do this using the input() function")

def get_input(prompt: str, type_converter):
    """This function will prompt the user for some input, and convert it using the type_converter type"""
    while True:
        try:
            return type_converter(input(prompt))
        except ValueError:
            print("Invalid input. Please try again.")

class Student:
    def __init__(self, name: str, age: int, school_level: int, gender: str, email: str, student_id: int):
        self.name = name
        self.age = age
        self.school_level = school_level
        self.gender = gender
        self.email = email
        self.student_id = student_id
        self.balance = 0.0

    def __str__(self):
        return f"This is {self.name}, a {self.age}-year-old {self.gender} student in grade {self.school_level}. You can reach them at {self.email}. Their student ID is {self.student_id}"

def create_student(school):
    name = get_input("Please enter the student's name: ", str)
    age = get_input("Please enter the student's age: ", int)
    school_level = get_input("Please enter the student's grade: ", int)
    gender = get_input("Please enter the student's gender: ", str)
    email = get_input("Please enter the student's email: ", str)
    if school:
        this_student_id = school[-1].student_id + 1
    else:
        this_student_id = 1
    return Student(name, age, school_level, gender, email, this_student_id)

school = []
"""
while True:
    # continue goes up here
    this_student = create_student()
    school.append(this_student)
    this_prompt = get_input("Would you like to add another student? (y/n): ", str).lower()
    if "n" not in this_prompt:
        continue
    else:
        break
# break goes down here
for student in school:
    print(student)
"""
range(3) == [0, 1, 2]

for number in range(3):
    this_student = create_student(school)
    school.append(this_student)

for student in school:
    print(student)

"""
name = get_input("Please enter your name: ", str)
age = get_input("Please enter your age: ", int)
truth = get_input("Please enter True or False: ", bool)
float_value = get_input("Please enter a float value: ", float)
print("You entered the following values:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Truth: {truth}")
print(f"Float Value: {float_value}")

some_variable = 10.1
if type(some_variable) == int:
    print("some_variable is an integer")
    print("I will now add to this integer")
    some_variable += 1
    print(f"The value is now {some_variable}")
elif type(some_variable) == float:
    print("some_variable is a float")
    print("I will now add to this float")
    some_variable += 1
    print(f"The value is now {some_variable}")
elif type(some_variable) == str:
    print("some_variable is a string")
elif type(some_variable) == bool:
    print("some_variable is a boolean")
else:
    print("some_variable is of an unknown type")
"""