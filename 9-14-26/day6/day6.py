file = open(r"day5/scratch.txt")
print(file)
file.close()

class something():
    def __init__(self):
        pass

this = something
print(this)

with open(r"day5/scratch.txt", "rb") as file:
    #for line in file:
        #print(line)
    line_list = file.readlines()
for index, line in enumerate(line_list):
    line_list[index] = line.strip()
print(line_list)
#the file is closed here