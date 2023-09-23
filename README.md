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

### Game Loop

![game-initialize](assets/images/game%20initialized.png)
![missed-battleship](assets/images/missed%20battleship.png)
![hit-battleship](assets/images/hit%20battleship.png)

### Error Handling
![error-handling](assets/images/game%20error%20handling%201.png)
![error-handling-2](assets/images/game%20error%20handling%202.png)
![error-handling-3](assets/images/game%20error%20handling%203.png)

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

I have successfully deployed Battleship Down on Heroku. Here are the steps i followed to deploy the game:

1. **Heroku Account** I signed up for a Heroku account at [Heroku's website](https://www.heroku.com/).

2. **Create New App** I selected to create new app on Heroku dashboard. I selected Python and Node.js as my buildpacks.

3. **Connected Github** I connected my Git hub account and the relevant repository

4. **Build App** Built the app in Heroku's virtual terminal 


## Contributions

Contributions to the game are welcome! If you have ideas for improvements or would like to report issues, feel free to create a pull request or an issue on the game's GitHub repository.


Enjoy playing Battleship Down and have fun sinking enemy battleships!



