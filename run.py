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

# Get the size of the game board from the user
size = get_input("Enter board size (Minimum size requirement: 5): ", minimum=5)
board = creat_board(size)

# Randomly determine the size, position, and orientation of the battleship
battleship_size = randint(1, size // 2)
battleship_row = randint(0, size - 1)
battleship_col = randint(0, size - 1)
battleship_orientation = (0, 1)

# Initialize game variables
sunk = False #Flag to check if battleship is sunk
turns = 0 # Keep track of the number of turns

# Main game loop
while not sunk:
    turns += 1
    print("\nTurn", turns)

    # Get the user's guess for row and column
    guess_row = get_input("Guess Row (1-{}): ".format(size), minimum=1, maximum=size)
    guess_col = get_input("Guess Col (1-{}): ".format(size), minimum=1, maximum=size)

    # Display the game board after each turn
    print_board(board)

    # Check if guessed coordinates hit the battleship
    if battleship_orientation == 0:
        if battleship_col <= guess_col - 1 < battleship_col + battleship_size:
            print("You hit a part of the battleship!")
            board[guess_row -1][guess_col - 1] = "X"
        else:
            print("You missed the battleship")
    else:
        if battleship_row <= guess_row - 1 < battleship_row + battleship_size:
            print("You hit part of the battleship!")
            board[guess_row - 1][guess_col - 1] = "X"
        else:
            print("You missed the battleship.")
    
    # Check if all parts of the battleship are hit
    if all(board[i][j] == "X" for i in range(battleship_row, battleship_row + battleship_size)
        for j in range(battleship_col, battleship_col + battleship_size)):
    print("Congratulations! You sank my battleship")
    sunk = True

# End of the game
print("Thanks for playing! It took you {} turns.".format(turns))

