import random
if __name__ == "__main__":
    """
    print("lists, dictionaries and loops")
    my_list = [0, 1, 2, 3, 4]
    index = len(my_list)
    index -= 1 # now it is == 4
    print(my_list[index])
    this_list = [0, "", True, 7 + 8, 15, [5, "True", ["I am here"]]]
    print(this_list[5][2][0])
    my_string = "Tomas Poventud"
    # print(my_string[2:4])
    for letter in my_string:
        print(letter)
    third_list = ["potato", "carrot", "peas"]
    for index, vegetable in enumerate(third_list):
        print(vegetable)
        if vegetable == "carrot":
            third_list[index] = "broccoli pea"
        print(vegetable)
    print(third_list)
    my_tuple = ("This", "tuple", "cannot", "change")
    print(my_tuple[2])
    my_tuple = ("This", "tuple", "can", "change")
    print(my_tuple[2])
    my_dict = {"key1": "value1", "key2": 2, "key3": True, "some_list": ["this list has a dict", {"key1": 1, "key2": "something"}], True: {7: 9}, "key2": "DEEP MYSTERIES"}
    print(my_dict)
    print(my_dict["key1"])
    print(my_dict["some_list"][1]["key2"])
    print(my_dict[True][7])
    for key, value in my_dict.keys():
        print(f"key: {key} has the value: {value}")
    my_dict["key2"] = "Holster"
    my_dict["new_key"] = False
    print(my_dict["key2"])
    print(my_dict["new_key"])
    my_dict["new_key"] = None
    print(my_dict["new_key"])
    the_value = my_dict.pop("new_key")
    print(the_value)
    my_set = {"apple", "orange", "orange", "banana"}
    print(my_set)
    my_set.update(["apple"])
    print(my_set)
    my_set.remove("apple")
    print(my_set)
    my_set.add("apple")
    print(my_set)
    my_set.discard("orangutan")
    print("Want to play a game?")
    my_lives = 10
    my_number = random.randint(0, 100)
    while my_lives > 0:
        guess = int(input("Guess my number"))
        if guess == my_number:
            print("You cheated somehow!")
            continue
        else:
            my_lives -= 1
            if guess < my_number:
                print("You guessed too low")
            else:
                print("You guessed too high")
    if my_lives == 0:
        print("You have died a terrible horrible death!")
    else:
        print("You get to live today...")
    """
    two_dimensional_list = [
            ["thing1", "thing2"],
            [None, 74],
            ["Shakira", "don't lie"]
        ]
    future_dict = {
        "key1": "value1",
        "something": "potato",
        "a list": [
            ["thing1", "thing2"],
            [None, 74],
            ["Shakira", "don't lie"]
        ],
        "...": "..."
    }
    print(two_dimensional_list[0][1])