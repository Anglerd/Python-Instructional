print("Today we will talk about if statements and their different uses")

# if (some_condition):
    # do something

# ==
# !=
# >
# <
# >=
# <=

# and
# or
# xor

if __name__ == "__main__":
    some_variable = 10
    another_variable = 10
    """
    if some_variable == 10 and another_variable == 20:
        print("Both conditions are true")
    if some_variable == 10 or another_variable == 30:
        print("At least one condition is true")
    if (some_variable == 10) ^ (another_variable == 30):
        print("Only one condition is true")
    
    #else if (This is invalid python syntax)
    if some_variable != 10:
        print("The first condition is true")
    elif another_variable != 20:
        print("The second condition is true")
    else:
        print("Neither condition is true")
    if some_variable == another_variable:
        print(f"some_variable: {some_variable} is another_variable: {another_variable}")
    elif some_variable < another_variable:
        print(f"some_variable: {some_variable} is less than another_variable: {another_variable}")
    else:
        # not (< or >), ==
        print(f"some_variable: {some_variable} is greater than another_variable: {another_variable}")
    """
    list_of_numbers = [1, 2, 3, 4, 5]
    list_of_strings = ["one", "two", "three", "four", "five"]
    list_of_lists = [[1, 2, 3, 4, 5], ["one", "two", "three", "four", "five"]]
    three_dimensional_list = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
    list_of_numbers[3] == 4
    list_of_strings[0] == "one"
    list_of_lists[1][1] == "two"
    three_dimensional_list[1][0][1] == 8
    # print(three_dimensional_list)
    # for number in list_of_numbers:
        # print(number)
    # for string in list_of_strings:
        # print(string)
    for inner_list in list_of_lists:
        for value in inner_list:
            print(value)
        print(inner_list)