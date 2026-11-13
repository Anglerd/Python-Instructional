def get_input(prompt, type_converter):
    while True:
        try:
            return type_converter(input(f"{prompt}\n"))
        except ValueError:
            print(f"Please enter a value of the type {type_converter}")

if __name__ == "__main__":
    """
    some_num = 10
    this_num = 10
    if some_num == this_num:
        print(f"some_num is equal to this_num, they are both: {some_num}")
    elif some_num < this_num:
        print(f"some_num ({some_num}) is less than this_num ({this_num})")
    else:
        print(f"some_num ({some_num}) is greater than this_num ({this_num})")
    your_num = get_input("What is your favorite number", float)
    if your_num:
        print(f"What a cool number! You can do so many things with {your_num}")
    else:
        print(f"I never thought of that before. {your_num} is a very interesting number")
    if your_num == some_num:
        print(f"How did you know that some_num was {some_num}")
    elif your_num < some_num:
        print(f"Why did you pick such a small number, you should have a number higher than {some_num}")
    print(bool(1))
    print(bool(-1))
    print(bool(0))
    print(bool(1.1))
    print(bool(0.5))
    print(bool(-0.4))
    print(bool(0.0))
    print(bool(-0))
    print(bool(-0.0))
    print(bool(""))
    print(bool("1"))
    print(bool("0"))
    print(bool([]))
    print(bool({}))
    print(bool(set()))
    print(bool(()))
    print(bool(None))
    print(True + True)
    if None == False:
        print("None is False!")
    else:
        print("None is not False!")
    some_string = "1abc"
    this_string = "ABC"
    if some_string == this_string:
        print("The strings are equal")
    elif some_string < this_string:
        print(f"some_string ({some_string}) is less than this_string ({this_string})")
    else:
        print(f"some_string ({some_string}) is greater than this_string ({this_string})")
    """
    print(True or False and not True)
    print(False and False)
    if True:
        pass
    elif True:
        pass
    else:
        pass
    if True:
        pass