"""Solution for day 4"""

import csv
import numpy as np

# Part 1

# Read numbers
with open("numbers.csv", encoding='UTF-8') as f:
    # Numbers file has only one row - using next on the reader to get it
    numbers_list = next(csv.reader(f))

# Convert numbers to integer
numbers_list = [int(n) for n in numbers_list]

# Read boards
board_array = []
board = []
with open("boards.csv", encoding='UTF-8') as f:
    # Read boards file (entries separated by spaces)
    boards_file = csv.reader(f, delimiter=' ')
    # Build array of boards (nested lists)
    for row in boards_file:
        # Remove in-between spaces (extra spaces before singe digit numbers) and convert to int
        board_line = [int(n) for n in row if n != '']
        if board_line:
            board.append(board_line)
        else:
            board_array.append(board)
            board = []

# Get numpy array for board
board_array_np = np.array(board_array)

# Get another array for marking drawn numbers
marking_array_np = np.zeros_like(board_array_np).astype(bool)

# Win BINGO
for number in numbers_list:
    # Mark number
    marking_array_np[board_array_np == number] = True
    # Check for BINGO
    column_bingo = np.any(np.all(marking_array_np, axis=1), axis=1)
    row_bingo = np.any(np.all(marking_array_np, axis=2), axis=1)
    winning_boards_np = np.logical_or(column_bingo, row_bingo)
    if np.any(winning_boards_np):
        # Get board where BINGO occurred
        board_id = np.squeeze(np.argwhere(winning_boards_np == True))
        last_number = number
        break

# Calculate scores
unmarked_sum = np.sum(board_array_np[board_id][marking_array_np[board_id] == False])
print(f"Result: {unmarked_sum*last_number}")
print(f"\tWinning board: {board_id}")
print(f"\tUnmarked sum: {unmarked_sum}")
print(f"\tLast number: {last_number}")
print("---------")

# Part 2

# Loose BINGO (we could continue from where the win algorithm termiated, but we start over again)
marking_array_np = np.zeros_like(board_array_np).astype(bool)
last_winning_boards = []

for number in numbers_list:
    # Mark number
    marking_array_np[board_array_np == number] = True
    # Check for BINGO
    column_bingo = np.any(np.all(marking_array_np, axis=1), axis=1)
    row_bingo = np.any(np.all(marking_array_np, axis=2), axis=1)
    winning_boards_np = np.logical_or(column_bingo, row_bingo)
    if np.any(winning_boards_np):
        # Check for BINGO on all boards
        if np.all(winning_boards_np):
            # Get board where last BINGO occurred
            board_id = [i for i in np.squeeze(np.argwhere(winning_boards_np == True)).tolist()
                        if i not in last_winning_boards][0]
            last_number = number
            break
    # Backup boards with BINGO
    last_winning_boards = np.squeeze(np.argwhere(winning_boards_np == True)).tolist()


# Calculate scores
unmarked_sum = np.sum(board_array_np[board_id][marking_array_np[board_id] == False])
print(f"Result: {unmarked_sum*last_number}")
print(f"\tLast board: {board_id}")
print(f"\tUnmarked sum: {unmarked_sum}")
print(f"\tLast number: {last_number}")
