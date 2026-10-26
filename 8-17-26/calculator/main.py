import calculations
import db_connector

def user_input_int(prompt=""):
    if prompt:
        prompt += "\n"
    try:
        return int(input(prompt))
    except ValueError:
        print("Please input a valid option")
def dissplay_menu():
    print("-----------------------------")
    print("Calculator with MySQL History Logger")
    print("-----------------------------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")
    print("5. Modulo (remainder)")
    print("6. Power")
    print("7. Get all calcs from DB")
    print("8. Exit")
    print("-----------------------------")
if __name__ == "__main__":
    while True:
        dissplay_menu()
        prompt = user_input_int()
        if prompt == 8:
            print("Goodbye")
            exit()
        if prompt == 7:
            calcs = db_connector.get_all_from_db()
            for calc in calcs:
                print(f"Calc number {calc[0]}, calculation performed {calc[1]}, with inputs ({calc[2]}, {calc[3]}, {calc[4]}) resulted in {calc[5]}. This calculation was performed at {calc[6]}. The following are the notes for this calculation {calc[7]}")
        else:
            num_1 = user_input_int("Please input the first number")
            num_2 = user_input_int("Please input the second number")
            notes = input("Would you like to add notes to this calculation in the DB? Simply type your note below, leave empty for no note.\n")
            if prompt == 1:
                result = calculations.add(num_1, num_2)
                calc_performed = "add"
                print(result)
            elif prompt == 2:
                result = calculations.sub(num_1, num_2)
                calc_performed = "sub"
                print(result)
            elif prompt == 3:
                result = calculations.mult(num_1, num_2)
                calc_performed = "mult"
                print(result)
            elif prompt == 4:
                num_3 = user_input_int("Please input the number of decimals to calculate")
                result = calculations.div(num_1, num_2, num_3)
                print(result)
                db_connector.save_calculation("div", result, num_1, num_2, num_3, notes)
            elif prompt == 5:
                result = calculations.mod(num_1, num_2)
                calc_performed = "mod"
                print(result)
            elif prompt == 6:
                result = calculations.pow(num_1, num_2)
                calc_performed = "pow"
                print(result)
            if prompt != 4:
                db_connector.save_calculation(calc_performed, result, num_1, num_2, notes=notes)
        if user_input_int("Would you like to exit? Type 1 to quit") == 1:
            print("Goodbye")
            exit()