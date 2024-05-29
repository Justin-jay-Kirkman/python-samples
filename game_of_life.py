# Conway's Game of Life https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
#
# Question:
#    Using any language, write a function that takes in a Conway's GOL board
#    and ouputs the next state of that board.
#
# Rules:
#    1. Any live cell with fewer than two live neighbors dies.
#    2. Any live cell with two or three live neighbors lives on to the next generation.
#    3. Any live cell with more than three live neighbours dies.
#    4. Any dead cell with exactly three live neighbors becomes a live cell.
#
# X         X X          X X
# X X   --> X   X   -->      X
#   X X     X X X        X   X
#
import copy
import random


class GameOfLife:
    def __init__(self, board):
        self.board = board

    def print_board(self, board=None):
        if board is None:
            board = self.board
        for row in board:
            print_row = ''
            for cell in row:
                if cell == 1:
                    print_row += "X "
                else:
                    print_row += "  "
            print(print_row)

    def next_board(self, board=None):
        if board is None:
            board = self.board
        new_board = copy.deepcopy(board)
        for x, row in enumerate(board):
            for y, column in enumerate(row):
                neighbors = 0
                current_cell = board[x][y]  # added for ease of reading

                # Kept these separate to show logic path - though can be refactored
                # top
                neighbors += self.find_neighbor(board, x - 1, y)
                # left
                neighbors += self.find_neighbor(board, x, y - 1)
                # right
                neighbors += self.find_neighbor(board, x, y + 1)
                # bottom
                neighbors += self.find_neighbor(board, x + 1, y)

                # top left
                neighbors += self.find_neighbor(board, x - 1, y - 1)
                # top right
                neighbors += self.find_neighbor(board, x - 1, y + 1)
                # bottom left
                neighbors += self.find_neighbor(board, x + 1, y + 1)
                # bottom right
                neighbors += self.find_neighbor(board, x + 1, y - 1)

                if current_cell == 1:
                    # 1. kill a cell
                    if neighbors < 2:
                        new_board[x][y] = 0
                    # 2. Lives on
                    if neighbors == 2 or neighbors == 3:
                        new_board[x][y] = 1
                    # 3. Gets starved out
                    if neighbors > 3:
                        new_board[x][y] = 0
                elif neighbors == 3 and current_cell == 0:
                    # 4. Born
                    new_board[x][y] = 1

        return new_board

    def find_neighbor(self, board, x, y):
        result = 0
        # add try exception for items larger than the list amount
        try:
            # prevent negative entries to not select from the right
            if board[x][y] == 1 and x >= 0 and y >= 0:
                result = 1
            else:
                result = 0
        except Exception as e:
            pass

        return result

    def max_run(self, limit):
        current_board = copy.deepcopy(board)
        for i in range(limit):
            print(f"------ Stage {i} -----")
            self.print_board(current_board)
            previous_board = copy.deepcopy(current_board)
            current_board = self.next_board(current_board)
            if current_board == previous_board:
                print("----- optimized -----")
                break

# Examples

# # 1 = Alive, 0 = Dead
board = [
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 1]
]

# Game = GameOfLife(board)
# Game.run(5)


# # 1 = Alive, 0 = Dead
random_range = random.randrange(1, 15)
board = [[random.randint(0, 1) for x in range(random_range)] for y in range(random_range)]
Game = GameOfLife(board)
Game.max_run(100)




