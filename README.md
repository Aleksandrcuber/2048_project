# A Game Of 2048

Hello! This is my try on a famous 2048 game

## Installation

To open the game, simply go to [this repository](https://github.com/Aleksandrcuber/2048_project.git) and run the `main.py` file of branch 'master'. You can use any version of Python newer then Python 3.6  
Or, optionally, you can run this:

```
git clone https://github.com/Aleksandrcuber/2048_project.git
python3 main.py
```

## Description of the code

To code this game, I use the ***MVC pattern*** here, which means we have three main sections of our programm.

The first one is **`Model.py`**, here we implement the inner logic of our game. This code processes every signal, received from the player, and changes state of the playing field in the corresponding way.

The second part of our project is **`View.py`**. Overall, it impements all the graphics for the game and also receives sygnals from the player. This part is not exactly ready yet, as the author is still not pretty comfortable with the Python's `tkinter` library. Hopefully it will be fixed soon!

The third, and the final part of our project is **`Controller.py`** file. It is responsible for receiving some sygnals from `View.py` (gotten from a player) and redirecting it to the `Model.py` file for the further working on that. Also it sends some commands to the `View.py` when necessary (to update state of the playing field, for example)

## How to play

As the programm starts, it will ask you size of the field you want to play on. Choose desired settings and press 'OK' button. Then the game will start.
Type in `w` to move up, `a` to move left, `s` to move down or `d` to move right. Every time playing field will be refreshed. You can also use arrow keys to do that. 
Make sure you are doing a possible move. If you type in a correct move which does not relocate any cells on the field, nothing will happen. Just type a new move instead.
Also you can press `undo` button to cancel previous move. You can do so several times in a row.
As soon as you get a 2048 cell on the field, you win! Game will notify yourself about that, but you can keep playing on that field just by agreeing to continue game. Otherwise a new game will be started.

If you run out of moves, you lose. Choose `Yes` to start over again, otherwise the programm will be stopped.

###### ***Hope you enjoyed!***
