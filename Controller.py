from View import *
from copy import deepcopy
from Inner_Settings import *


class MyStack:
    def __init__(self, start_value):
        self.list = [start_value]

    def __len__(self):
        return len(self.list)

    def push(self, elem):
        if len(self) >= MAX_QUEUE_DEPTH:
            self.list.pop(0)
        self.list.append(elem)

    def pop(self):
        if len(self) == 1:
            return None
        return self.list.pop()

    def last(self):
        if len(self) == 0:
            return None
        else:
            return self.list[-1]


class Controller:
    def __init__(self, model):
        self.model = model
        self.__history = MyStack(deepcopy(model))
        self.view = None

    def set_view(self, view):
        self.view = view

    def start_game(self):
        self.view.refresh_from_model()
        self.view.start_loop()

    def handle_the_move(self, flag):
        if flag == 'undo':
            self.undo_move()
            return
        if flag not in ['w', 'a', 's', 'd']:
            self.view.handle_wrong_input()
            return
        was_won = self.model.check_win()
        if not self.model.move(flag):
            return
        self.view.refresh_from_model()
        self.__history.push(deepcopy(self.model))
        if self.model.check_win() and not was_won:
            if self.view.handle_win():
                self.__history = MyStack(deepcopy(self.model))
                return
            else:
                self.restart_game()
        if self.model.is_lost():
            if self.view.handle_loss():
                self.restart_game()
            else:
                self.quit()

    def undo_move(self):
        elem = self.__history.pop()
        if elem is None:
            return
        prev_model = deepcopy(self.__history.last())
        self.model = prev_model
        self.view.reset_model(prev_model)
        self.view.refresh_from_model()


    @staticmethod
    def quit():
        exit()

    def restart_game(self):
        self.view.reset()
