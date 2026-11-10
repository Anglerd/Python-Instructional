"""
print("Hello, World!")

integer = 3
a_float = 3.14
another_float = 2.0
string = "Tomas Poventud😈"
boolean = True
second_bool = False

print(integer)
print(a_float)
print(another_float)
print(string)
print(boolean)
print(second_bool)

print(0.1 + 0.2)
"""
"""
0
1
2
3
4
5
6
7
8
9
10
11

0
1
2
3
4
5
6
7
8
9
A
B
C
D
E
F
10
11

0
1
10
11
100
101
110
111
"""

# 0 000000000000 0000000000000000000 # messed up representation of a float (should be 64 bits), sign bit, some exponent bits, some mantissa bits

def will_crash(some_parameter, second_parameter):
    print(some_parameter)
    print(second_parameter)
    return 1 / second_parameter  # will crash if second_parameter is 0

def will_crash2():
    will_crash("Hello, World!", 0)

class Student():
    def __init__(self, name, school_year, grades):
        self.name = name
        self.year = school_year
        grades = grades

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def graduate(self):
        self.year += 1
        grades = []

    def get_GPA(self):
        return sum(self.grades)/len(self.grades)

MY_SECRET = "Please don't look at my secret, it is secret!" # this "secret" is a global variable that can be accessed from any file that imports this file

if __name__ == "__main__": # this block (everything on the indentation below) of code will only run if this file is run directly, not if it is imported into another file
    print("This is part of the \"main\" block")
    something_valuable = 1
    if something_valuable == 1:
        print("something_valuable is equal to 1") # this is still part of the "main" block
    integer_2 = 2
    some_other_float = 9.9
    this_string = "This is a string"
    my_true = True
    if integer_2:
        integer_2 += some_other_float
    print(integer_2)
    # print(this_string * integer_2)
    # print(((True or False) and not True))
    """
    some_student = Student("Tomas Poventud", 1)
    second_student = Student("Bob", 12)
    print(f"{some_student.name} is the name of the student in year {some_student.year}")
    print(f"{second_student.name} is the name of the student in year {second_student.year}")
    some_student.graduate()
    print(f"{some_student.name} is the name of the student in year {some_student.year}")
    print(f"{second_student.name} is the name of the student in year {second_student.year}")
    """
    print("I will be printed with the number!", integer_2)
    print(f"I will be printed with the number! {integer_2}")
print("Unconditional print statement")