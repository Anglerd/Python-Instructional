# Object Oriented Programming (OOP)

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


class Student:
    def __init__(self):
        self.name = input("Please enter your name: ")
        self.course = input("Please enter the course name: ")
        self.week = input_int("Please enter the training week number: ")
        self.day = input_int("Please enter the training day number: ")
        self.debt = 0.0

    def __str__(self):
        return f"Student Name: {self.name}\nCourse Name: {self.course}\nTraining Week: {self.week}\nTraining Day {self.day}\nAccount Balance: ${self.debt:.2f}"

    def change_name(self, new_name):
        self.name = new_name

    def add_to_balance(self, amount):
        self.debt += amount

    def subtract_from_balance(self, amount):
        if amount > self.debt:
            print("Overcharge Error! You cannot overpay your debt.")
        else:
            self.debt -= amount

if __name__ == "__main__":
    print(r'\"Welcone to day 2\\1 of the \n Python Programming course\"')
    print(r"E:\Random Stuff\Certification Classes\Python Instructional\8-17-26")
    print("E:\\Random Stuff\\Certification Classes\\Python Instructional\\8-17-26")
    print('today we are learning variables, input and syntax')
    print('"We are building a student intake script"')

    print("""This is a multi-line string that will be printed as-is,
    without any special character interpretation.""")

    """
    input_student_name = input("Please enter your name: ")
    print("This line will not print until the user has entered their name and pressed Enter.")
    print(f"Student Name: {input_student_name}")
    while True:
        try:
            input_training_week = int(input("Please enter the training week number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the training week number.")
    print(f"Training Week: {input_training_week}")
    """
    student1 = Student()
    print(student1)
    print("You have lied to me, your name is actually Gary")
    student1.change_name("Gary")
    print(student1)
    print("Welcome to class you are now charged $100")
    student1.add_to_balance(100.0)
    print(student1)
    if input("Would you like to pay off your debt? y/n\n").lower().__contains__("y"):
        student1.subtract_from_balance(100.0)
    else:
        student1.add_to_balance(10000.0)
        print("How dare you not give me money!")
    print(student1)