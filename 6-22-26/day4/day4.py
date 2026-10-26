my_list = ["string1", "string2", "string3.1"]
# my_list = [["s"], [t], [r], [i]...]
my_dictionary = {"Shakira": {"Shakira's info": "hips"}, "Tracy": "lies"}
# "name": {info}

# sub_string part of the string, in this case "stri"

for str in my_dictionary:
    inner_object = my_dictionary[str]
    # print(str)
    # print(inner_object)
    # print(str)
    if isinstance(inner_object, dict):
        for second_str in inner_object:
            # print(second_str)
            # inner_object[second_str]
            print(inner_object[second_str])
    else:
        print(inner_object)