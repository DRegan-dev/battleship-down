# Import the randint function from the random module
from random import randint

# Function to create a game board of a given size
def create_board(b_size):
    board = []
    for i range(b_size):
        board.append([0] * b_size)
    return board