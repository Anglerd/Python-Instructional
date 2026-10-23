if __name__ == "__main__":
    print("let's talk about (bruno) lists (which are arrays if you know what that means) dictionaries, and iteration")
    a_list = [0, 1, 2, 3, 4, 5]
    a_list[3] == 3
    list2 = [7, 5, 6, 8, 9, 0]
    list2[3] == 8
    list_of_stuff = [1, 2.2, True, "some_string", [0, 1, 2]]
    list_of_stuff[2] == True
    list_of_stuff[1] == 2.2
    list_of_stuff[3] == "some_string"
    print(list_of_stuff[3])
    big_list = range(100)
    for juliet, harry in enumerate(list_of_stuff):
        print(f"at index {juliet}, the value is {harry}")
    two_d_list = [[0, 1], [2, 3]]
    two_d_list[0] == [0, 1]
    two_d_list[1] == [2, 3]
    print(two_d_list[1])
    print(two_d_list[1][0])
    small_list = [
        1,
        2,
        3
    ]
    one_line_dict = {"key1": "value1", "key2": 2}
    some_dict = {
        "key1": 1,
        "key_key": "Foofoo",
        "hermione": "wingardium",
        "Gerald": 4,
        "this_list": [4, 1],
        2: "something",
        True: "hurts my soul",
        3.3: "just ugly"
    }
    print(one_line_dict)
    print(some_dict[True])
    print(some_dict[3.3])
    # dictionaries have 3 "main" methods items, values, and keys
    """
    for key, value in some_dict.items():
        print(f"In some_dict at key {key}, the value is {value}")
    for key in some_dict:
        print(some_dict[key])
    """
    #tuple
    #set
    my_tuple = (0, 1, 2, 3)
    a_list.append(7)
    print(a_list)
    a_list[2] = 9
    print(a_list)
    print(my_tuple)
    my_tuple = (0, 0, 0, 0)
    print(my_tuple)
    fruit = {"apple", "banana", "orange"}
    print(fruit)
    fruit.add("apple")
    print(fruit)
    fruit.add("tomato")
    print(fruit)
    fruit.discard("cherry")
    print(a_list)
    number = a_list.pop()
    print(number)
    print(a_list)
    number = a_list.remove(len(a_list) // 2)
    print(a_list)
    print(number)
    six_list = [0, 1, 2, [4, 5, 6], 4, 9]
    print(len(six_list))
    print(len(one_line_dict))
    print(len(my_tuple))
    print(len(fruit))
    """
    for(int i = 0; i < len(six_list); i++) {
        print(six_list[i])
    }
    """
    student = {
        "name": "Harry Harrison",
        "age": 15,
        "gender": "M",
        "grade": 54,
        "year": 5
    }
    for key in student:
        print(f"{student["name"]}'s {key} is {student[key]}")