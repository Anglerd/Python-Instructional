import day1.day1 as day1
from random import randint, random


day1.paid_a_lot_of_money()
print(randint(0, 10))
print(random())

print(day1.global_var)

# Python is an object oriented language
class Student:
    def __init__(self, name):
        self.name = name
        self.debt = 0

    def name_change(self, new_name):
        old_name = self.name
        self.name = new_name
        return old_name

    def get_name(self):
        return self.name

    def __str__(self):
        return f"This is {self.name}, and they have ${self.debt} debt"

    #def __repr__(self):
    #    return f"{self.name} has ${self.debt} debt"

if __name__ == "__main__":
    a_string = "\tThis is tabbed"
    print(a_string)
    a_string = b"\tThis is tabbed"
    print(a_string)
    tomas = Student("Tomás Poventud")
    print(tomas)
    original_name = tomas.name_change("Immanuel Kant")
    print(tomas)
    print(tomas.get_name())
    str(tomas)
    print(original_name)
    second_student = Student("Rebecca Black")
    print(second_student)
    tomas.debt = tomas.debt + 20 # tomas.debt += 20
    print(tomas)
    second_student.name_change("Kumar")
    print(second_student)
    a_list = [1, 2, 3]