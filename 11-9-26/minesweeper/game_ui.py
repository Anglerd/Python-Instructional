import pygame
# pip install pygame-ce pygbag
import asyncio
import minefield
import db_connector
import time

# -----------SETTINGS---------
MARGIN = 40 # margin between window edge and the box
TOP_MARGIN = 50
BG_COLOR = (20, 20, 30)
BOX_COLOR = (200, 200, 200) # white
CLICKED_BOX = (100, 100, 100) # gray
CELL_SIZE = 20
MENU_BUTTON_WIDTH = 400
MENU_BUTTON_HEIGHT = 20

NUMBER_COLORS = {
    1: (25, 90, 220), 2: (30, 140, 40), 3: (210, 40, 40), 4: (20, 20, 130),
    5: (130, 20, 20), 6: (20, 130, 130), 7: (0, 0, 0), 8: (90, 90, 90),
}

DIFFICULTY = {
    "Easy": {
        "num_rows": 5,
        "num_columns": 5,
        "number_of_bombs": 4
    },
    "Medium": {
        "num_rows": 6,
        "num_columns": 6,
        "number_of_bombs": 8
    },
    "Hard": {
        "num_rows": 6,
        "num_columns": 8,
        "number_of_bombs": 11
    },
    "Very Hard": {
        "num_rows": 7,
        "num_columns": 10,
        "number_of_bombs": 21
    },
    "Impossible": {
        "num_rows": 8,
        "num_columns": 12,
        "number_of_bombs": 44
    }
}

RADIUS = 15
SPEED = 250

def generate_squares(row_num, column_num):
    output = []
    for local_x in range(row_num):
        output.append([])
        for local_y in range(column_num):
            output[local_x].append(pygame.Rect(MARGIN + local_y * CELL_SIZE, MARGIN + local_x * CELL_SIZE + TOP_MARGIN, CELL_SIZE, CELL_SIZE))
    return output

async def get_load():
    pygame.init()
    board_dicts = db_connector.get_all_games_from_db()
    num_games = len(board_dicts)
    screen = pygame.display.set_mode((MARGIN * 2 + MENU_BUTTON_WIDTH, MARGIN * 2 + MENU_BUTTON_HEIGHT * num_games))
    pygame.display.set_caption("Load a game from DB")
    load_boxes = []
    font = pygame.font.Font(None, 28)
    for index, this_game in enumerate(board_dicts):
        load_boxes.append(pygame.Rect(MARGIN, MARGIN + index * MENU_BUTTON_HEIGHT, MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT))
        pygame.draw.rect(screen, BOX_COLOR, load_boxes[index], width=1)
        this_dict = board_dicts[index]
        rendered_difficulty = font.render(f"{this_dict["minefield_id"]}. {this_dict["difficulty"]} {this_dict["num_column"]}x{this_dict["num_row"]}", True, (200, 200, 200))
        screen.blit(rendered_difficulty, ((MARGIN, MARGIN + MENU_BUTTON_HEIGHT * index), (MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT)))
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # left click
                        for index, proposed_board in enumerate(board_dicts):
                            if load_boxes[index].collidepoint(event.pos):
                                chosen_board = proposed_board
                                game_board = db_connector.get_all_cells_from_game(chosen_board["minefield_id"], chosen_board["num_row"], chosen_board["num_column"])
                                number_of_bombs = 0
                                for local_x in range(chosen_board["num_row"]):
                                    for local_y in range(chosen_board["num_column"]):
                                        if game_board[local_x][local_y].get("num_board", 0) == 9:
                                            number_of_bombs += 1
                                running = False
            await asyncio.sleep(0)
        pygame.quit()
        return chosen_board["difficulty"], chosen_board["num_row"], chosen_board["num_column"], number_of_bombs, game_board, chosen_board["board_id"]

async def menu():
    pygame.init()
    num_difficulties = len(DIFFICULTY)
    screen = pygame.display.set_mode((MARGIN * 2 + MENU_BUTTON_WIDTH, MARGIN * 2 + MENU_BUTTON_HEIGHT * num_difficulties + TOP_MARGIN)) # TOP_MARGIN for space for load from db button
    pygame.display.set_caption("Minesweeper Main Menu")
    difficulty_rects = []
    font = pygame.font.Font(None, 28)
    load_box = pygame.Rect(MARGIN, MARGIN, MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT)
    pygame.draw.rect(screen, CLICKED_BOX, load_box, width=1)
    load_text = font.render("Load a game from DB?", True, (200, 200, 200))
    screen.blit(load_text, ((MARGIN, MARGIN), (MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT)))
    for index, this_difficulty in enumerate(DIFFICULTY):
        difficulty_rects.append(pygame.Rect(MARGIN, MARGIN + index * MENU_BUTTON_HEIGHT + TOP_MARGIN, MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT))
        pygame.draw.rect(screen, BOX_COLOR, difficulty_rects[index], width=1)
        this_dict = DIFFICULTY[this_difficulty]
        rendered_difficulty = font.render(f"{this_difficulty} {this_dict["num_columns"]}x{this_dict["num_rows"]} {this_dict["number_of_bombs"]} bombs", True, (200, 200, 200))
        screen.blit(rendered_difficulty, ((MARGIN, MARGIN + MENU_BUTTON_HEIGHT * index + TOP_MARGIN), (MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT)))
    pygame.display.flip()
    running = True
    load_game = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click
                    for local_x, difficulty in enumerate(DIFFICULTY):
                        this_cell = difficulty_rects[local_x]
                        if this_cell.collidepoint(event.pos):
                            difficulty_chosen = difficulty
                            chosen_dict = DIFFICULTY[difficulty_chosen]
                            running = False
                    if load_box.collidepoint(event.pos):
                        load_game = True
                        running = False
        await asyncio.sleep(0)
    pygame.quit()
    if load_game:
        return None, None, None, None, None, None
    return difficulty_chosen, chosen_dict["num_rows"], chosen_dict["num_columns"], chosen_dict["number_of_bombs"], None, None
    

async def main(row_num=5, column_num=5, number_of_bombs=4, game_board=None, difficulty="Easy"):
    pygame.init()
    screen = pygame.display.set_mode((MARGIN * 2 + column_num * CELL_SIZE, MARGIN * 2 + row_num * CELL_SIZE + TOP_MARGIN))
    cells = generate_squares(row_num, column_num)
    pygame.display.set_caption("Minesweeper")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 28)
    game_state = True
    running = True
    # game_loop starts
    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click
                    for local_x in range(row_num):
                        for local_y in range(column_num):
                            this_cell = cells[local_x][local_y]
                            if this_cell.collidepoint(event.pos):
                                if not game_board:
                                    while True:
                                        game_board = minefield.make_field(row_num, column_num, number_of_bombs)
                                        if game_board[local_x][local_y].get("num_bomb", 0) == 0:
                                            for sub_local_x in range(row_num):
                                                for sub_local_y in range(column_num):
                                                    game_board[sub_local_x][sub_local_y]["revealed"] = False
                                                    game_board[sub_local_x][sub_local_y]["flagged"] = False
                                                    if game_board[sub_local_x][sub_local_y].get("num_bomb", 0) == 0:
                                                        game_board[sub_local_x][sub_local_y]["num_bomb"] = 0
                                            board_id = db_connector.save_board(difficulty, row_num, column_num, game_board)
                                            break
                                minefield.do_reveal(game_board, local_x, local_y, row_num, column_num, board_id)
                                if game_board[local_x][local_y].get("num_bomb", 0) == 9:
                                    running = False
                                    win_state = False
                                    game_state = False
                                else:
                                    num_check = True
                                    for local_x in range(row_num):
                                        for local_y in range(column_num):
                                            if game_board[local_x][local_y].get("num_bomb", 0) != 9 and not game_board[local_x][local_y].get("revealed", False):
                                                num_check = False
                                    if num_check:
                                        running = False
                                        win_state = True
                                        game_state = False
                # TODO add right click flag
        screen.fill(BG_COLOR)
        for local_x in range(row_num):
            for local_y in range(column_num):
                this_reveal = False
                if game_board and game_board[local_x][local_y].get("revealed", False):
                    this_reveal = True
                pygame.draw.rect(screen, CLICKED_BOX if this_reveal else BOX_COLOR, cells[local_x][local_y], width=1)
                if this_reveal:
                    num_bomb = font.render(str(game_board[local_x][local_y].get("num_bomb")), True, NUMBER_COLORS.get(game_board[local_x][local_y].get("num_bomb"), 1))
                    screen.blit(num_bomb, ((MARGIN + local_y * CELL_SIZE, MARGIN + local_x * CELL_SIZE + TOP_MARGIN), (CELL_SIZE, CELL_SIZE)))
        # TODO TIMER AND BOMB COUNTER GO BELOW SIMILAR TO HOW BOUNCES USED TO WORK FOR BALL_GAME
        """
        label = font.render(f"Bounces: {bounces}    (click to change color)", True, BOX_COLOR)
        screen.blit(label, (MARGIN, 10))
        """
        pygame.display.flip()
        await asyncio.sleep(0)
    # game_loop ended
    if not game_state:
        db_connector.delete_game_from_db(board_id)
        if win_state: # on win flash screen green
            for _ in range(5):
                screen.fill((0, 255, 0))
                pygame.display.flip()
                time.sleep(2)
                screen.fill((0, 0, 0))
                pygame.display.flip()
                time.sleep(2)
        else: # on win flash screen red
            for _ in range(5):
                screen.fill((255, 0, 0))
                pygame.display.flip()
                time.sleep(2)
                screen.fill((0, 0, 0))
                pygame.display.flip()
                time.sleep(2)
    pygame.quit()

if __name__ == "__main__":
    difficulty, num_row, num_column, number_of_bombs, game_board, board_id = asyncio.run(menu())
    if not difficulty:
        difficulty, num_row, num_column, number_of_bombs, game_board, board_id = asyncio.run(get_load())
    asyncio.run(main(num_row, num_column, number_of_bombs, game_board, difficulty, board_id))