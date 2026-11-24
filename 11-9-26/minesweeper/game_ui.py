import pygame
# pip install pygame-ce pygbag
import asyncio
import random

# -----------SETTINGS---------
MARGIN = 40 # margin between window edge and the box
TOP_MARGIN = 20
BG_COLOR = (20, 20, 30)
BOX_COLOR = (200, 200, 200) # white
CLICKED_BOX = (100, 100, 100) # gray
CELL_SIZE = 20
MENU_BUTTON_WIDTH = 200
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
    clicked_cells = []
    for local_x in range(row_num):
        output.append([])
        clicked_cells.append([])
        for local_y in range(column_num):
            output[local_x].append(pygame.Rect(MARGIN + local_y * CELL_SIZE, MARGIN + local_x * CELL_SIZE + TOP_MARGIN, CELL_SIZE, CELL_SIZE))
            clicked_cells[local_x].append(False)
    return output, clicked_cells

async def menu():
    pygame.init()
    num_difficulties = len(DIFFICULTY)
    screen = pygame.display.set_mode((MARGIN * 2 + num_difficulties * MENU_BUTTON_WIDTH, MARGIN * 2 + MENU_BUTTON_HEIGHT * CELL_SIZE + TOP_MARGIN)) # TOP_MARGIN for space for load from db button
    pygame.display.set_caption("Minesweeper Main Menu")
    difficulty_rects = []
    for index, this_difficulty in enumerate(DIFFICULTY):
        difficulty_rects.append(pygame.Rect(MARGIN, MARGIN + index * MENU_BUTTON_HEIGHT + TOP_MARGIN, MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT))
    # TODO Draw all menu selections
    running = True
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
        await asyncio.sleep(0)
    pygame.quit()
    # TODO use difficulty chosen to return the correct board_size
    

async def main(row_num=5, column_num=5, number_of_bombs=4, game_board=None):
    pygame.init()
    screen = pygame.display.set_mode((MARGIN * 2 + column_num * CELL_SIZE, MARGIN * 2 + row_num * CELL_SIZE + TOP_MARGIN))
    # TODO change clicked_cells to game_board logic as in main.py
    cells, clicked_cells = generate_squares(row_num, column_num)
    pygame.display.set_caption("Minesweeper")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 28)
    running = True
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
                                clicked_cells[local_x][local_y] = True
        screen.fill(BG_COLOR)
        for local_x in range(row_num):
            for local_y in range(column_num):
                this_clicked = clicked_cells[local_x][local_y]
                pygame.draw.rect(screen, CLICKED_BOX if this_clicked else BOX_COLOR, cells[local_x][local_y], width=1)
                if this_clicked:
                    num_bomb = font.render(str(SOME_KINDA_NUM_BOMB), True, NUMBER_COLORS.get(SOME_KINDA_NUM_BOMB, 1))
                    screen.blit(num_bomb, ((MARGIN + local_y * CELL_SIZE, MARGIN + local_x * CELL_SIZE + TOP_MARGIN), (CELL_SIZE, CELL_SIZE)))
        # TODO TIMER AND BOMB COUNTER GO BELOW SIMILAR TO HOW BOUNCES USED TO WORK FOR BALL_GAME
        """
        label = font.render(f"Bounces: {bounces}    (click to change color)", True, BOX_COLOR)
        screen.blit(label, (MARGIN, 10))
        """
        pygame.display.flip()
        await asyncio.sleep(0)
    pygame.quit()

if __name__ == "__main__":
    asyncio.run(main(10, 15))