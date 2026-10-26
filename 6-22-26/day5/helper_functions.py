def file_opener(file_path):
    '''This is a simple function that will open and read files "automagically" and handle certain common errors.
    Returns an array of lines that have been stripped on success.
    Returns none whenever an error has occured''' # this is header text that will be shown whenever help(file_opener) is called, which is by default done whenver the function is "hovered" over
    try:
        return_array = []
        this_file = open(file_path, "r")
        for line in this_file:
            return_array.append(line.rstrip()) # on the return_array append the lines that have been right stripped (stripped of whitespace from the right)
        this_file.close() # even though the file is expected to close as soon as the function exits we should still close as good practice
        return return_array
    except FileNotFoundError:
        print("The specified file was not found")
    # more excepts can be added as follows
    # except OSError:
        # print("Could not open/read file")
    return None

def pythonic_file_opener(file_path):
    '''This is a simple function that will open and read files "automagically" and handle certain common errors. Written to be more "Pythonic"
    Returns an array of lines that have been stripped on success.
    Returns none whenever an error has occured'''
    try:
        with open(file_path, "r") as this_file:
            return [line.rstrip() for line in this_file] # note the lack of "close" as using "with" closes file_path for us on break of scope
        # also note the use of an inline for loop (read as "do_this for this in something") that is immediately encased in an array
        # in general for python if it can read as "english" it is generally correct
    except FileNotFoundError:
        print("The specified file was not found")
    return None

if __name__ == "__main__":
    some_file = "some_test_file"
    print(file_opener(some_file))
    print(pythonic_file_opener(some_file))