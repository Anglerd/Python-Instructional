import random

# TODO BIG ONE! change all x to row, change all y to column, including in DB, rename field to cell (matching DB)
def number_to_coord(number: int, n: int):
    out_x = number % n # 0 to x if we go over x then we go back to 0
    out_y = number // n # only goes up if over x, e.x. 0 to x == 0 then x to 2 * x == 1 etc.
    return out_x, out_y

def make_field(row: int, column: int, number_of_bombs: int):
    """Makes any sized board for minesweeper inserting a number of bombs mostly randomly, currently possible to make "gambling" boards. ALWAYS REFERENCE CELLS WITH GET, THEY DON'T HAVE DEFAULT VALUES"""
    # field = [[{} for _ in range(column)] for _ in range(row)]
    field = []
    for row_index in range(row):
        field.append([])
        for _ in range(column):
            field[row_index].append({})
    while number_of_bombs > 0:
        this_x, this_y = number_to_coord(random.randint(0, row * column - 1), row) # get a random number in range of the minefield, convert that number to a x, y coordinate
        proposed_cell = field[this_x][this_y].get("num_bomb", 0)
        if proposed_cell != 9:
            field[this_x][this_y]["num_bomb"] = 9
            number_of_bombs -= 1 # TODO make purely solvable boards?
            # add hints to fields surrounding bombs
            for num_x in range(-1, 2):
                local_x = this_x + num_x
                if local_x >= row or local_x < 0:
                    continue
                for num_y in range(-1, 2):
                    local_y = this_y + num_y
                    if local_y >= column or local_y < 0:
                        continue
                    try:
                        if field[local_x][local_y]["num_bomb"] != 9:
                            field[local_x][local_y]["num_bomb"] += 1
                    except KeyError:
                        field[local_x][local_y]["num_bomb"] = 1
    return field

if __name__ == "__main__":
    test_board = make_field(10, 12, 50)
    for row in test_board:
        print(row)