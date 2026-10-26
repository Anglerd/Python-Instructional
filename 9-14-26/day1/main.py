"""
my_name = "Tomás Poventud123😈" # string put some crazy stuff behind the comment symbol
my_age = 31 # int (short for integer)
my_temperature = 98.6 # float
my_truth = True # boolean

def my_function(some_parameter):
    print("This is my function")
    print("My name is", my_name)
    print("My age is", my_age)
    print("My temperature is", my_temperature)
    print("My truth is", my_truth)
    print("The parameter I passed in is", some_parameter)

if __name__ == "__main__":
    print("My name is", my_name)
    print("My age is", my_age)
    print("My temperature is", my_temperature)
    print("My truth is", my_truth)

    print("My name is " + my_name)
    print("My age is " + str(my_age)) # 31 integer "31" string

# object oriented programming
class Student:
    def __init__(self, name, age, school_level):
        self.name = name
        self.age = age
        self.school_level = school_level

    def age_up(self):
        self.age += 1
        self.school_level += 1

    def introduce(self):
        print("Hello, my name is", self.name)
        print("I am", self.age, "years old")
        print("I am in", self.school_level, "grade")

this_student = Student("Tomás Poventud", 31, 4)
this_student.name = "Dominick Rodriguez" # changing the name of the student object
this_student.age_up() # calling the age_up method to increase the age by 1
this_student.introduce()
"""

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.incidences = 0

    def accident(self):
        self.tires -= 1
        self.incidences += 1
        print("The car has been in an accident and now has", self.tires, "tires.")

    def car_fax(self):
        print("The car is a", self.year, self.make, self.model, "It has been in", self.incidences, "accidents.")

    def repair(self):
        if self.tires < 4:
            self.tires += 1
        print("The car has been repaired and now has", self.tires, "tires.")

my_garage = []

car1 = Car("Chevy", "Equinox", 2016)
car2 = Car("Toyota", "Camry", 2020)
car3 = Car("Honda", "Civic", 2018)

my_garage.append(car1)
my_garage.append(car2)
my_garage.append(car3)

for car in my_garage:
    car.car_fax()

my_garage[0] # Chevy Equinox 2016
my_garage[1] # Toyota Camry 2020

my_dict = {}
key = "my_key"
my_dict[key] = "my_value"
print(my_dict["my_key"])

set1 = {1, 2, 3, 4, 5}
set1.add(1) # adding a duplicate value to the set

my_tuple = (1, 2, 3, 4, 5)
# my_tuple[0] = 10 # trying to change a value in the tuple
print(my_tuple[0])