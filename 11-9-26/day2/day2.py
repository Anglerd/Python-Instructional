def get_input(prompt, type_converter):
    while True:
            try:
                return type_converter(input(f"{prompt}\n"))
            except ValueError:
                print(f"Invalid input, please enter a value of the type {type_converter}")

def validate_input(prompt, valid_list, type_converter: Type = str):
    while True:
        this_input = get_input(prompt, type_converter)
        if type_converter == str:
            temp_input = this_input.lower()
        else:
            temp_input = this_input
        if temp_input in valid_list:
            return this_input
        else:
            print(f"That is not avalid input, please enter one of the following {valid_list}")

class Car:
    def __init__(self, tires, make, model, year, car_class):
        self.tires = tires
        self.make = make
        self.model = model
        self.year = year
        self.car_class = car_class
        self.carfax = 0

    def accident(self):
        self.tires -= 1 if self.tires > 0 else 0
        self.carfax += 1

    def repair(self):
        self.tires += 1 if self.tires < 4 else 0

    def __str__(self):
        if self.tires == 1:
            tire_suffix = ""
        else:
            tire_suffix = "s"
        if self.carfax == 1:
            accident_suffix = ""
        else:
            accident_suffix = "s"
        return f"This {self.make} {self.model} was made in {self.year}. It is a {self.car_class} that currently has {self.tires} tire{tire_suffix}, and has been in {self.carfax} accident{accident_suffix}"

def main():
    """
    car_classes = ["sedan", "hatchback", "suv", "truck"]
    this_class = validate_input("What is the class of this car?", car_classes)
    this_car_tires = validate_input("How many tires does this car start with?", range(5), int)
    this_car = Car(this_car_tires, input("What is the make of this car?"), input("What is the model of this car?"), get_input("What year was this car made", int), this_class)
    print(this_car)
    this_car.accident()
    print(this_car)
    this_car.repair()
    print(this_car)
    this_car.accident()
    this_car.accident()
    this_car.repair()
    this_car.repair()
    this_car.repair()
    this_car.repair()
    print(this_car)
    """
    print(f"After adding 1 and 2 we get {1 + 2}")
    print(f"In python the truthiness of 0 is {bool(0)}")
    print(bool(0))
    # True if condition else False
    print(f"When checking my inline if I find: {"This is my weird statement" if 1 == 0 else "Only normal things here"}")

if __name__ == "__main__":
    main()
