import random

def number_to_coord(number: int, x: int):
    out_x = number % x # 0 to x if we go over x then we go back to 0
    # TODO fix out of range, 120 // 10 == 12 which is out of range
    out_y = number // x # only goes up if over x, e.x. 0 to x == 0 then x to 2 * x == 1 etc.
    return out_x, out_y

def make_field(x: int, y: int, num_bombs: int):
    """Makes any sized board for minesweeper inserting a number of bombs mostly randomly, currently possible to make "gambling" boards"""
    field = []
    for _ in range(x):
        field.append([0] * y)
    this_dist = random.randint(0, x * y)
    while num_bombs > 0:
        this_x, this_y = number_to_coord(this_dist, x)
        proposed_cell = field[this_x][this_y]
        if proposed_cell != 9:
            proposed_cell = 9
            num_bombs -= 1 # TODO make purely solvable boards?
            # add hints to fields surrounding bombs
            for num_x in range(-1, 2):
                local_x = this_x + num_x
                # TODO fix bombs wrapping around and breaking cells when they are on x = 0 or y = 0
                if local_x >= x or local_x < 0:
                    continue
                for num_y in range(-1, 2):
                    local_y = this_y + num_y
                    if local_y >= y or local_y < 0:
                        continue
                    if field[local_x][local_y] != 9:
                        field[local_x][local_y] += 1
        this_dist = random.randint(0, x * y)
    return field

if __name__ == "__main__":
    test_board = make_field(10, 12, 50)
    for row in test_board:
        print(row)