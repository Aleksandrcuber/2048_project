# A Game Of 2048

Hello! This is my try on a famous 2048 game

## Installation

To open the game, simply go to [this repository](https://gitlab.akhcheck.ru/aleksandr.gerasimov/2048_project.git) and run the `main.py` file of branch 'master'. You can use any version of Python newer then Python 3.6. But make sure you've installed `pygame` Python's library. If you haven't, you can do it by executing ```pip install pygame``` in your terminal.
  
Or, optionally, you can run this:

```
git clone https://gitlab.akhcheck.ru/aleksandr.gerasimov/2048_project.git
pip install pygame
python3 main.py
```

## Description of the code

To code this game, I use the ***MVC pattern*** here, which means we have three main sections of our programm.

The first one is **`Model.py`**, here we implement the inner logic of our game. This code processes every signal, received from the player, and changes state of the playing field in the corresponding way. This also stores all the data about the state of the game and the players (this will be released in the futuree)

The second part of our project is **`View.py`**. Overall, it impements all the graphics for the game and also receives sygnals from the player.

The third, and the final part of our project is **`Controller.py`** file. It is responsible for receivingsome sygnals from `View.py` (gotten from a player) and redirecting it to the `Model.py` file for the further working on that. Also it sends some commands to the `View.py` when necessary (to update state of the playing field, for example)


## How to play

As the programm starts, it will ask you size of the field you want to play on. Also you can choose music and colour scheme. Select desired settings and press 'Submit' button. Then the game will start.
Type in `w` to move up, `a` to move left, `s` to move down or `d` to move right. Every time playing field will be refreshed. You can also use arrow buttons on the screen or arror keys on your keyboard to do that. 
Make sure you are doing a possible move. If you type in a correct move which does not relocate any cells on the field, nothing will happen. Just type a new move instead.
Also you can press `undo` button to cancel previous move. You can do so several times in a row.
As soon as you get a 2048 cell on the field, you win! Game will notify yourself about that, but you can keep playing on that field just by agreeing to continue game. Otherwise a new game will be started.

If you run out of moves, you lose. Choose `Yes` to start over again, otherwise the programm will be stopped.

Note: if you want to try this game in console, you can do so by going to `Inner_Settings.py` file and setting `DO_INTERFACE` variable to `False`.

###### ***Hope you enjoyed!***
