from Controller import *
from Model import *
from Console_Interface import *
from Graphic_Interface import *


class View:
    def __init__(self, do_graphics=False):
        self.model = None
        self.controller = None
        if do_graphics:
            self.interface = Window()
        else:
            self.interface = Console()
        self.model, self.controller = self.__ask_settings()
        self.controller.set_view(self)

    def __ask_settings(self):
        rows, cols = self.interface.ask_settings()
        try:
            model = Field(rows, cols)
        except SizeError:
            model = Field()
        controller = Controller(model)
        return model, controller

    def reset_model(self, model):
        self.model = model

    def refresh_from_model(self):
        self.interface.refresh(self.model)

    def start_loop(self):
        self.interface.start_loop(self.controller)

    def handle_win(self):
        return self.interface.handle_win(self.model)

    def handle_loss(self):
        return self.interface.handle_loss(self.model)

    def handle_wrong_input(self):
        self.interface.wrong_input()

    def reset(self):
        self.model, self.controller = self.__ask_settings()
        self.controller.set_view(self)
        self.controller.start_game()
