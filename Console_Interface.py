# from View import *


class Console:
    @staticmethod
    def __print_options():
        print("Type 'w', 'a', 's' or 'd' to make a move, 'restart' to restart the game,"
              " 'undo' to cancel last move and 'exit' to to quit the game")

    def ask_settings(self):
        self.__print_options()
        cont_to_ask = True
        rows, cols = 0, 0
        while cont_to_ask:
            try:
                rows, cols = map(int, input("Input size of playing field: ").split())
            except (ValueError, TypeError):
                print("You entered something wrong! Input two numbers, divided by space")
            else:
                cont_to_ask = False
        return rows, cols

    def refresh(self, model):
        print()
        self.__print_result(model)
        print("Number of moves:", model.moves)
        print()
        self.__print_array(model.get_table())
        print("=" * 20)

    def handle_win(self, model):
        print("CONGRATULATIONS!!!")
        print("YOU WON!", end=' ')
        self.__print_result(model)
        return input("Would you like to continue this game? [y/n]").strip() == 'y'

    def handle_loss(self, model):
        print("Out of moves!")
        print("You lost!", end=' ')
        self.__print_result(model)
        return input("Would you like to start new game? [y/n]").strip() == 'y'

    @staticmethod
    def start_loop(controller):
        string = input().strip()
        while string != 'restart' and string != 'exit':
            controller.handle_the_move(string)
            string = input().strip()
        if string == 'restart':
            controller.restart_game()
        else:
            controller.quit()

    @staticmethod
    def __print_result(model):
        print("Your current result is", model.curr_result())

    @staticmethod
    def __print_array(lst):
        for row in lst:
            for elem in row:
                print(str(elem) + ' ' * (7 - len(str(elem))), end=' ')
            print()

    @classmethod
    def wrong_input(cls):
        print("You entered something wrong!")
        cls.__print_options()
