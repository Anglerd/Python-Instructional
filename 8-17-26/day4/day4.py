some_list = ["some", "stuff", ["this", "list", "is", "inside"]]
textbook_square_array_of_2x2 = [["car", "book"], ["school", "person"]]
textbook_square_array_of_2x2[0] == ["car", "book"]
textbook_square_array_of_2x2[0][1] == "book"
some_dictionary = {"key": "value"}
some_dictionary["key"] == "value"

use_this = [1, 7, "this", "something", 2, 8, "more", "this list goes on"]

this_list_is_huge = []
for num in range(10000):
    this_list_is_huge.append(num)

range(4) == [0, 1, 2, 3]
"""
for some_crazy_name in this_list_is_huge:
    #this give us only the values in the list
    print(some_crazy_name)
    
for index, value in enumerate(use_this):
    #this gives us both the value and the index of the list that the value came from
    print(f"At index {index} the value of the list is {value}")
"""
example_dictionary = {"key1": "value1", "key2": 2, "key3": 7, "key4": ["car", "book"], "most_important": "Shakira's hips"}
example_dictionary["key1"] == "value1"
example_dictionary["key2"] == 2

for key in example_dictionary:
    print(example_dictionary[key])

some_string = "some string"

some_string[0] == "s"

some_string[0:3] == "some"
some_string[:3] == "some"
some_string[-1] == "g"
some_string[-7:-1] == "string"

print(some_string)

#print(use_this[0:3])

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student_with_class = Student("John Doe", 3.5)

student_directory_with_dictionary = {
    "name": "John Doe",
    "age": 3.5
}

for character in some_string:
    print(character)