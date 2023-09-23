# Import the randint function from the random module
from random import randint, choice

# Function to create a game board of a given size
def create_board(b_size):
    board = []
    for i in range(b_size):
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
            cell = board[j - 1][i]
            # Check if the cell contains a hit or a miss
            if cell == "H":
                print("H", end=" ")
            elif cell == "M":
                print("M", end=" ")
            else:
                print("0", end=" ")
            
        print()

# Function to get user input with optional minimum and maximum constraints
def get_input(prompt, minimum = None, maximum = None):
    while True:
        try:
            value = int(input(prompt))
            if (minimum is not None and value < minimum) or (maximum is not None and value > maximum):
                print("Input must be between {} and {}".format(minimum, maximum))
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def place_battleship(board, size):
    while True:
        row = randint(0, size-1)
        col = randint(0, size - 1)
        orientation = choice(["horizontal", "vertical"])

        if orientation == "horizontal":
            if col + size <= len(board[0]):
                valid_position = True
                for i in range(size):
                    if board[row][col + i] == "X":
                        valid_position = False
                        break
                if valid_position:
                    for i in range(size):
                        if board[row][col + i] == "X":
                            return row, col, orientation
        else:
            if row + size <= len(board):
                valid_position = True
                for i in range(size):
                    if board[row + i][col] == "X":
                        valid_position = False
                        break
                if valid_position:
                    for i in range(size):
                        board[row + i][col] = "X"
                    return row, col, orientation
                

# Print a welcome message
print("Welcome to Battleship Down!\n")
print("Please input your guess using numbers only. Press enter to submit your guess.")

# Get the size of the game board from the user
while True:
    size = get_input("Enter board size (Minimum size requirement: 5): ", minimum=5, maximum=100)
    if size >= 5:
        break
    else:
        print("Board size must be at least 5.")

board = create_board(size)

# Randomly determine the size, position, and orientation of the battleship
battleship_size = randint(1, size // 2)
battleship_row, battleship_col, battleship_orientation = place_battleship(board, battleship_size)

# Initialize game variables
sunk = False #Flag to check if battleship is sunk
turns = 0 # Keep track of the number of turns
unhit_turns = 0 # Maximum number of consecutive turns without hitting the battleship
max_unhit_turns = 10 # Keep track of consecutive unhit turns

# Track the number of hits on the battleship
hits = 0

# Main game loop
while not sunk:
    turns += 1
    unhit_turns += 1
    print("\nTurn", turns)

    # Get the user's guess for row and column
    guess_row = get_input("Guess Row (1-{}): ".format(size), minimum=1, maximum=size)
    guess_col = get_input("Guess Col (1-{}): ".format(size), minimum=1, maximum=size)

    # Display the game board after each turn
    print_board(board)

    # Check if guessed coordinates hit the battleship
    if board[guess_row - 1][guess_col - 1] == "X":
        print("You hit a part of the battleship!")
        board[guess_row - 1][guess_col - 1] = "H"
        unhit_turns = 0
        hits += 1
    else:
        print("You missed the battleship")
    
    if unhit_turns >= max_unhit_turns:
        print("The battleship has changed its position.")
        board = create_board(size)
        battleship_row, battleship_col, battleship_orientation = place_battleship(board, battleship_size)
        unhit_turns = 0

    # Check if all parts of the battleship are hit
    if hits == battleship_size:
        print("Congratulations! You sank my battleship")
        sunk = True

# End of the game
print("Thanks for playing! It took you {} turns.".format(turns))

