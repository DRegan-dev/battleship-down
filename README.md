# Battleship Down

![Battleship-image](assets/images/_bb54b26a-a32c-46d1-becb-6213028c6f87.jpeg)

Battleship Down is a classic console game where you take on the role of a naval commander and attempt to sink an enemy battleship hidden somewhere on the game board. This README provides essentail information about the game, how to play it, and additional details

## Game Overview ##
In Battleship Down, your mission is to locate and sink the enemy battleship, which is hidden on a grid based gane board. Here are the key components of the game:

* ### Game Board: ### A grid of user-defined size where you make your guesses.

* ### Battleship: ### An enemy battleship of randowm size, position, and orientation on the board

* ### Turns: ### The game is played in turns. You make guesses to find and sink the battleship.

* ### Unhit Turns: ### If you have a certain number of consecutive unhit turns, the battleship changes its position.

* ### Winning: ### The game ends when you successfully hit and sink all parts of the battleship.

## How to Play ##

1. ** Welcome Message: ** When you start the game, you'll receive a friendly welcome message.

2. ** Board Size Selection: ** You'll be prompted to enter the size of the game board. The minimum required size is 5, and the maximum is 100. 

3. ** Battleship Setup: ** The game randomly determines the size, position, and orientation of the battleship

4. ** Game Loop: ** The game enters the main loop, where you attempt to sink the battleship. The loop continues until the battleship is sunk.

5. ** Guessing the Battleship: ** In each turn, make a guess by entering row and column coordinates on the game board.

6. ** Feedback: ** After each guess, the game provides feedback. Hits are marked as "H" on the board, misses are notified. 

7. ** Changing Battleship Position: ** If you have a certain number of consecutice unhit turns(as defined by `max-unhit-turns`), the battleship changes its posotion, and the board is reset

8. ** Winning the Game: ** The game continues until you successfully hit and sink allparts of the battleship. You win the game, and the number of turns it took you is displayed. 

9. ** End of the Game: ** The game concludes withe a "Thanks for playing!" message .

## Screenshots ##
## Testing ## 

Detailed testing was performed on the Battleship Down game to ensure its functionality and stability. The following aspects were tested:

* **Game Board Creation:** Ensured that the game board is correctly generated with the user-defined size. 

* **Battleship Placement:** Verified that the battleship is placed randomly on thebored with the correct size and orientation. 

* **User Input Handling:** Tested the user input functions to ensure they accept valid input and handle invalid input gracefully.

* **Game Logic:** Checked that the game logic correctly identifies hits, misses, and the sinking of the battleship. 

* **Battleship Position Change:** Confirmed that the battleship changes position after a vertian number of consecutive unhit turns.

## Used Libraries

The game utilizes the following Python libraries:

* `random`: Used for randomisation of battleship placement and other game elements.

## Technologies Used

* **Python:** The game is implemented in Python.

* **Command-Line Interface (CLI):** The game runs in the console using the command-line interface

## Deployment

## Contributions

## License

Enjoy playing Battleship Down and have fun sinking enemy battleships!



## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
