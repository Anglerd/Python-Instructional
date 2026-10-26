def get_input(prompt, type_converter):
    while True:
        try:
            return type_converter(input(f"{prompt}\n"))
        except ValueError:
            print(f"Please enter a valid input of type {type_converter}")