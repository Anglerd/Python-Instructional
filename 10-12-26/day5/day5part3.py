def get_input(prompt, type_converter):
    while True:
        try:
            return type_converter(input(f"{prompt}\n"))
        except ValueError:
            print(f"Please enter a valid input of the type {type_converter}")

def menu_options():
    print("-----------------------------------------------")
    print("Please pick an option from below")
    print("-----------------------------------------------")
    print("1. View hotels with their ratings and locations")
    print("2. Add a hotel")
    print("3. save and quit")

if __name__ == "__main__":
    with open(r".\day5\output.csv") as f:
        hotels = []
        for line in f:
            line = line.strip().split(",")
            hotels.append({
                "name": line[0],
                "rating": line[1],
                "location": line[2]
            })
    user_choice = None
    while user_choice != 3:
        menu_options()
        user_choice = get_input("", int)
        if user_choice == 1:
            for this_hotel in hotels:
                print(this_hotel)
        elif user_choice == 2:
            while True:
                proposed_hotel = {}
                proposed_hotel["name"] = input("Enter the hotel's name")
                proposed_hotel["rating"] = get_input("Enter the hotel's rating", float)
                proposed_hotel["location"] = input("Enter the hotel's location")
                if "y" in input(f"You have entered: {proposed_hotel}, if this is correct enter y to submit").lower():
                    break
            hotels.append(proposed_hotel)
    # here they have chosen option 3
    file_writer = ""
    for this_hotel in hotels:
        file_writer += f"{this_hotel["name"]},{this_hotel["rating"]},{this_hotel["location"]}\n"
    with open(r".\day5\output.csv", "w") as f:
        f.write(file_writer)