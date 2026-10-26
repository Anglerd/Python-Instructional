def my_input(some_string):
    while True:
        try:
            return input(some_string)
        except ValueError:
            print("That was an invalid input, please try again")

def my_num_input(some_string):
    while True:
        try:
            return int(my_input(some_string))
        except ValueError:
            print("That was an invalid input, please input a number")

def choose_alignment():
    this_alignment = my_input("Enter your alignment as the 2 initial letters, for example Lawful Good would be LG, Chaotic Neutral would be CN: ").lower().strip()
    if "l" in this_alignment:
        some_number = 0
    elif "c" in this_alignment:
        some_number = 2
    else:
        some_number = 1
    if "g" in this_alignment:
        some_number += 0
    elif "e" in this_alignment:
        some_number += 6
    else:
        some_number += 3
    return some_number

def prompt_adjective():
    some_info = {}
    some_info["adjective"] = my_input("Enter the adjective you would like to add to the database: ")
    some_info["alignment"] = choose_alignment()
    print(f"This adjective is {some_info['adjective']} and it is for alignment {some_info['alignment']}")
    return some_info

def prompt_character():
    some_info = {}
    some_info["name"] = my_input("Enter character name: ")
    some_info["alignment"] = choose_alignment()
    some_info["weapon"] = my_input(f"Enter a weapon for {some_info['name']}: ")
    some_info["level"] = int(my_num_input(f"Enter the current level of {some_info['name']}: "))
    print(f"""This characters name is {some_info["name"]} they are alignment {some_info["alignment"]}
          their weapon is {some_info["weapon"]} their level is {some_info["level"]}""")
    return some_info

def prompt_action():
    some_info = {}
    some_info["pc_name"] = my_input("Enter the character name that performed the action: ")
    some_info["action"] = my_input(f"Enter the action performed by {some_info['pc_name']} ")
    some_info["result"] = my_input(f"Enter the result of {some_info['action']} (leave blank if no result): ")
    print(f"{some_info['pc_name']} {some_info['action']} which caused (if any) {some_info['result']}")
    return some_info


if __name__ == "__main__":
    # prompt_character()
    prompt_action()