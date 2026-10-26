if __name__ == "__main__":
    """
    for count in range(10):
        
        if count == 2:
            print(f"{count} is only somewhat inportant")
        if count > 5 and count < 7:
            print(f"count is between 5 and 7, specifically it is {count}")
        elif count == 1:
            print("1 is more important and will not associate with the other rules")
        elif count < 4 or count > 8:
            print(f"count is outside of 4 and 8, specifically it is {count}")
        elif count == 9:
            print("this will never appear")
        else:
            print(f"count is 4, 5, 7, or 8. specifically it is {count}")
        print(f"{count} is really cool") if count == 0 else print(f"{count} is not cool")

        
        match count:
            case 2:
                print(f"{count} is only somewhat inportant")
                print(f"count is outside of 4 and 8, specifically it is {count}")
            case 6:
                print(f"count is between 5 and 7, specifically it is {count}")
            case 1:
                print("1 is more important and will not associate with the other rules")
            case _ if count < 4 or count > 8:
                print(f"count is outside of 4 and 8, specifically it is {count}")
            case 9:
                print("this will never appear")
            case _:
                print(f"count is 4, 5, 7, or 8. specifically it is {count}")
        """
    while True:
        while True:
            try:
                cool_num = int(input("Please type a number to check its coolness\n"))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        if cool_num == 0:
            print(f"{cool_num} IS cool")
        elif cool_num == 7:
            print(f"{cool_num} is SUPER COOL!!!")
        else:
            print(f"{cool_num} is NOT cool")
        # print(str(cool_num) + (" IS cool" if cool_num == 0 else " is SUPER COOL!!!" if cool_num == 7 else " is NOT cool"))
        should_exit = input("Would you like to go again? y/n\n").lower()
        if "n" in should_exit:
            break

def some_function(some_parameters=7, some_other_parameters=9) -> str:
    """This is a docstring that will be read whenver the "help" function is called. This is noremally done when this function is hovered over in most IDE's"""
    some_string = ""
    return some_string