if __name__ == "__main__":
    print("We are going to open and manipulate files today")
    print("Opening a file is almost exactly the same as using the input() function")
    f = open("scratch.txt", "rt")

    # r - read-only
    # a - append (add on to the end of the file)
    # w - write
    # x - create (returns an error if the file already exists)

    # b - byte-mode b"\n\t"
    # t - text-mode """
    #    """

    """
    for line in f:
        print(line.strip())
    """
    """
    lines = f.readlines()
    for this_line in lines:
        print(this_line.strip())
    """
    raw_file = f.read()
    print(raw_file)
    f.close()
    with open(r".\day5\starting questions.txt") as questions:
        lines = questions.readlines()
        print(lines)
    with open(".\\day5\\hotels.csv") as hotels:
        hotel_list = []
        for line in hotels:
            #continue goes here
            #if "something":
            #    continue
            line = line.strip().split(",")
            # print(line)
            #.append("something to append")
            """
            .append(
            "something to append"
            )"""
            hotel_list.append({
                "name": line[0],
                "rating": line[1],
                "location": line[2]
            })
            print(hotel_list[-1])
    for hotel in hotel_list:
        hotel["rating"] = 10
    print(hotel_list)
    my_file_write = ""
    for hotel in hotel_list:
        my_file_write += f"{hotel["name"]} {hotel["rating"]} {hotel["location"]}\n"
    writing_file = open(".\\day5\\output.csv", "w")
    writing_file.write(my_file_write)
    writing_file.close()
    # questions is closed here