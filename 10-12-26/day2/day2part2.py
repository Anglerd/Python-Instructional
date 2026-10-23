def get_input(prompt, type_converter):
    while True:
        try:
            return type_converter(input(f"{prompt}\n"))
        except ValueError:
            print(f"Please input a correct value of the type {type_converter}")

def validate_input(prompt, type_converter, range):
    proposed_input = get_input(prompt, type_converter)
    while proposed_input not in range:
        print(f"Please enter a value in the range of {range}")
        proposed_input = get_input(prompt, type_converter)
    return proposed_input

class Student:
    def __init__(self):
        self.name = input("Enter this student's name")
        self.grade = validate_input(f"Please enter {self.name}'s, grade", int, range(101))
        proposed_school_year = validate_input(f"Enter {self.name}'s school year (6-8)", int, [6, 7, 8])
        if proposed_school_year == 6:
            self.year = 6
        elif proposed_school_year == 7:
            self.year = 7
        else:
            self.year = 8
        """
        if get_input("Enter anything for male, nothing for Female", bool):
            self.gender = "Male"
        else:
            self.gender = "Female"
        """
        if "y" in input(f"Is {self.name} a male? y/n").lower():
            self.gender = "Male"
        else:
            self.gender = "Female"

    def __str__(self):
        return f"{self.name} is a {self.gender} in year {self.year}. Their current grade is {self.grade}"

if __name__ == "__main__":
    """
    some_input = input("I will prompt the user for input\n")
    print(f"You just typed {some_input}")
    print("You just typed " + some_input)
    print(f"You just typed {some_input} which I think is a little funny")
    print("You just typed " + some_input + " which I think is a little funny")
    some_number = get_input("Please enter a number", str) # after typing 6 will be "6" instead of 6 or 6.0
    if some_number == 6:
        print("Wow what an amazing number")
    """
    student_num = get_input("Enter the number of students you would like to create", int)
    """
    count = 0
    while count < student_num:
        do_stuff
        count += 1
    """
    school = []
    for _ in range(student_num):
        school.append(Student())
    for student in school:
        print(student)

"""
char first_language = "c"
char superlative = "with some variables"
char second_language = "python"
"This is an f string in %s %s which is different than %s", first_language, superlative, second_language
"This is an f string in c with some variables which is different than python"
"""

some_name_with_multiple_words = ""
_some_weird_name = ""

#not allowed
123_some_variable
illegal-name-2
illegal - name - 2
this is 4 variables
print = "DONT DO THIS"

for_name_in_list = ["some", "crazy", "list"]