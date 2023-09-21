# Import the randint function from the random module
from random import randint

# Function to create a game board of a given size
def create_board(b_size):
    board = []
    for i range(b_size):
        board.append([0] * b_size)
    return board

# Function to print the game board
def print_board(board):
    # Print column numbers
    print("  ", end=" ")
    for i in range(1, len(board[0]) + 1):
        print(i, end=" ")
    print()

    for j in range(1, len(board) + 1):
        print(j, end=" ")
        for i in range(len(board[0])):
            print(board[j -1][i], end=" ")
        print()

# Function to get user input with optional minimum and maximum constraints
def get_input(prompt, minimum=None, Maximum=None):
    while True:
        try:
            value = int(input(prompt))
            if (minimum is not None and value < minimum) or (maximum is not None and value > maximum):
                print("Input must be between {} and {}".format(minimum, maximum))
                continue
            return value
        except ValueError:
            print("You must enter a valid number.")

# Print a welcome message
print("Welcome to Battleship Down!\n")
print("Please input your guess using numbers only. Press enter to submit your guess.")

