import tkinter as tk
import pygame
import random
from tkinter.ttk import Combobox
from tkinter.messagebox import askyesno
from View import *
from Inner_Settings import *
import time


class Window:
    def __init__(self):
        self.controller = None
        self.music = None
        self.colors = Standard()
        self.row_num = 0
        self.col_num = 0
        self.cells = []
        self.need_field_configure = False

        self.window = tk.Tk()
        self.window.wm_protocol("WM_DELETE_WINDOW", self.__ask_to_quit)
        self.window.withdraw()
        self.window.title("2048 Game")
        self.window["bg"] = self.colors.MAIN_BG_COLOR

        self.dialog = tk.Toplevel()
        self.dialog.withdraw()
        self.dialog.title("Choose settings")
        self.__dialog_init()

        self.stats = tk.Frame(self.window, bg=self.colors.MAIN_BG_COLOR)
        self.result = tk.Label(self.stats, text='', bg=self.colors.STATS_COLOR, height=2)
        self.result.pack(side=tk.LEFT)
        self.moves = tk.Label(self.stats, text='', bg=self.colors.STATS_COLOR, height=2)
        self.moves.pack(side=tk.RIGHT)
        self.stats.pack(fill=tk.X, side=tk.TOP, padx=5, pady=(10, 5))

        self.main_field = tk.Frame(self.window, bg=self.colors.MAIN_BG_COLOR)
        self.main_field.rowconfigure(index=0, weight=1)
        self.main_field.columnconfigure(index=0, weight=1)

        self.field = tk.Frame(self.main_field, bg="#ffffff", relief="ridge", borderwidth=3)
        self.field.grid(column=0, row=0, sticky="nsew")

        self.button_moves = tk.Frame(self.main_field, bg=self.colors.MAIN_BG_COLOR)
        self.__make_move_buttons(self.button_moves)
        self.button_moves.grid(column=4, row=0, padx=(30, 10), sticky="nsew")

        self.main_field.pack(fill=tk.BOTH, padx=5, pady=(10, 10), expand=True)

        self.extra_butts = tk.Frame(self.window, bg=self.colors.MAIN_BG_COLOR)
        self.extra_butts.pack(fill=tk.X, side=tk.BOTTOM, padx=5, pady=5)
        self.undo_butt = tk.Button(self.extra_butts, borderwidth=1, bg=self.colors.BUTTON_BG_COLOR, fg=self.colors.BUTTON_FG_COLOR, text="Undo", font=("Times New Roman", 18))
        self.undo_butt.pack(side=tk.LEFT)
        self.exit_butt = tk.Button(self.extra_butts, borderwidth=1, bg=self.colors.BUTTON_BG_COLOR, fg=self.colors.BUTTON_FG_COLOR, text="Exit", font=("Times New Roman", 18))
        self.exit_butt.pack(side=tk.RIGHT, padx=10)
        self.restart_butt = tk.Button(self.extra_butts, borderwidth=1, bg=self.colors.BUTTON_BG_COLOR, fg=self.colors.BUTTON_FG_COLOR, text="Restart", font=("Times New Roman", 18))
        self.restart_butt.pack(side=tk.RIGHT, padx=10)

        self.messages = tk.Label(self.window, text='', bg=self.colors.MAIN_BG_COLOR, fg=self.colors.MAIN_FG_COLOR, height=3, font=("Times New Roman", 22))
        self.messages.pack(fill=tk.X, side=tk.BOTTOM, padx=5, pady=5)

    def __dialog_init(self):
        self.dialog["bg"] = self.colors.MAIN_BG_COLOR
        for i in range(2):
            self.dialog.rowconfigure(index=i, minsize=50, weight=1)
            self.dialog.columnconfigure(index=i, minsize=50, weight=1)
        self.dialog.rowconfigure(index=2, minsize=50, weight=1)
        self.dialog.rowconfigure(index=3, minsize=50, weight=1)
        self.dialog.rowconfigure(index=4, minsize=50, weight=1)

        self.lbl_num_rows = tk.Label(self.dialog,
                                height=1,
                                text="Number of lines: ",
                                bg=self.colors.MAIN_BG_COLOR,
                                font=("Times New Roman", 18),
                                foreground=self.colors.MAIN_FG_COLOR)
        self.box_num_rows = Combobox(self.dialog, state="readonly", justify=tk.RIGHT, font=("Times New Roman", 16), width=6)
        self.box_num_rows['values'] = [i for i in range(4, 11)]
        self.box_num_rows.current(0)
        self.lbl_num_rows.grid(row=0, column=0, sticky='nsew')
        self.box_num_rows.grid(row=0, column=1)

        self.lbl_num_cols = tk.Label(self.dialog,
                                height=1,
                                text="Number of columns: ",
                                bg=self.colors.MAIN_BG_COLOR,
                                font=("Times New Roman", 18),
                                foreground=self.colors.MAIN_FG_COLOR)
        self.box_num_cols = Combobox(self.dialog, state="readonly", justify=tk.RIGHT, font=("Times New Roman", 16), width=6)
        self.box_num_cols['values'] = [i for i in range(4, 11)]
        self.box_num_cols.current(0)
        self.lbl_num_cols.grid(row=1, column=0, sticky='nsew')
        self.box_num_cols.grid(row=1, column=1)

        self.lbl_music = tk.Label(self.dialog,
                             height=1,
                             text="Music on the background: ",
                             bg=self.colors.MAIN_BG_COLOR,
                             font=("Times New Roman", 18),
                             foreground=self.colors.MAIN_FG_COLOR)
        self.choose_song = Combobox(self.dialog, state="readonly", justify=tk.RIGHT, font=("Times New Roman", 16), width=6)
        self.choose_song['values'] = ["OFF", "Minecraft", "Beethoven", "Chopin"]
        self.choose_song.current(0)
        self.lbl_music.grid(row=2, column=0, sticky="nsew")
        self.choose_song.grid(row=2, column=1)

        self.lbl_colors = tk.Label(self.dialog,
                             height=1,
                             text="Colour scheme: ",
                             bg=self.colors.MAIN_BG_COLOR,
                             font=("Times New Roman", 18),
                             foreground=self.colors.MAIN_FG_COLOR)
        self.choose_color = Combobox(self.dialog, state="readonly", justify=tk.RIGHT, font=("Times New Roman", 16), width=6)
        self.choose_color['values'] = ["Standard", "Bright", "Dark"]
        self.choose_color.current(0)
        self.lbl_colors.grid(row=3, column=0, sticky="nsew")
        self.choose_color.grid(row=3, column=1)

        self.btn_submit = tk.Button(self.dialog, text='SUBMIT', fg=self.colors.BUTTON_FG_COLOR, bg=self.colors.BUTTON_BG_COLOR, font=("Times New Roman", 20), command=self.__submit_changes)
        self.btn_submit.grid(row=4, column=0, columnspan=2, pady=(10, 1), sticky='nsew')

    def __make_move_buttons(self, parent):
        for i in range(5):
            parent.rowconfigure(index=i, weight=1, minsize=50)
            parent.columnconfigure(index=i, weight=1, minsize=50)
        self.left_button = tk.Button(parent,
                                borderwidth=2,
                                width=7,
                                foreground=self.colors.BUTTON_FG_COLOR,
                                background=self.colors.BUTTON_BG_COLOR,
                                text="\N{LEFTWARDS ARROW}",
                                command=lambda: self.controller.handle_the_move("a")
                                )
        self.left_button.grid(row=2, column=1, sticky="nsew")
        self.up_button = tk.Button(parent,
                              borderwidth=2,
                              width=7,
                              foreground=self.colors.BUTTON_FG_COLOR,
                              background=self.colors.BUTTON_BG_COLOR,
                              text="\N{UPWARDS ARROW}",
                              command=lambda: self.controller.handle_the_move("w")
                              )
        self.up_button.grid(row=1, column=2, sticky="nsew")
        self.right_button = tk.Button(parent,
                                 borderwidth=2,
                                 width=7,
                                 foreground=self.colors.BUTTON_FG_COLOR,
                                 background=self.colors.BUTTON_BG_COLOR,
                                 text="\N{RIGHTWARDS ARROW}",
                                 command=lambda: self.controller.handle_the_move("d"))
        self.right_button.grid(row=2, column=3, sticky="nsew")
        self.down_button = tk.Button(parent,
                                borderwidth=2,
                                width=7,
                                foreground=self.colors.BUTTON_FG_COLOR,
                                background=self.colors.BUTTON_BG_COLOR,
                                text="\N{DOWNWARDS ARROW}",
                                command=lambda: self.controller.handle_the_move("s"))
        self.down_button.grid(row=3, column=2, sticky="nsew")

    def ask_settings(self):
        self.__place_window(self.dialog)
        self.dialog.deiconify()
        self.dialog.wm_protocol("WM_DELETE_WINDOW", self.__submit_changes)
        self.dialog.mainloop()
        return self.row_num, self.col_num

    def __submit_changes(self):
        self.row_num = int(self.box_num_rows.get())
        self.col_num = int(self.box_num_cols.get())
        self.music = Music(self.choose_song.get())
        new_color = self.choose_color.get()
        if new_color == "Standard":
            self.colors = Standard()
        elif new_color == "Dark":
            self.colors = Dark()
        else:
            self.colors = Bright()
        self.need_field_configure = True
        self.dialog.withdraw()
        self.dialog.quit()

    def __update_colors(self):
        self.window["bg"] = self.colors.MAIN_BG_COLOR
        self.dialog["bg"] = self.colors.MAIN_BG_COLOR
        self.stats['bg'] = self.colors.MAIN_BG_COLOR
        self.result['bg'] = self.colors.STATS_COLOR
        self.moves['bg'] = self.colors.STATS_COLOR
        self.main_field['bg'] = self.colors.MAIN_BG_COLOR
        self.button_moves['bg'] = self.colors.MAIN_BG_COLOR
        self.extra_butts['bg'] = self.colors.MAIN_BG_COLOR
        self.undo_butt['fg'] = self.colors.BUTTON_FG_COLOR
        self.undo_butt['bg'] = self.colors.BUTTON_BG_COLOR
        self.restart_butt['fg'] = self.colors.BUTTON_FG_COLOR
        self.restart_butt['bg'] = self.colors.BUTTON_BG_COLOR
        self.exit_butt['fg'] = self.colors.BUTTON_FG_COLOR
        self.exit_butt['bg'] = self.colors.BUTTON_BG_COLOR
        self.messages['bg'] = self.colors.MAIN_BG_COLOR
        self.messages['fg'] = self.colors.MAIN_FG_COLOR
        self.lbl_colors['bg'] = self.colors.MAIN_BG_COLOR
        self.lbl_colors['fg'] = self.colors.MAIN_FG_COLOR
        self.lbl_num_cols['bg'] = self.colors.MAIN_BG_COLOR
        self.lbl_num_cols['fg'] = self.colors.MAIN_FG_COLOR
        self.lbl_num_rows['bg'] = self.colors.MAIN_BG_COLOR
        self.lbl_num_rows['fg'] = self.colors.MAIN_FG_COLOR
        self.lbl_music['bg'] = self.colors.MAIN_BG_COLOR
        self.lbl_music['fg'] = self.colors.MAIN_FG_COLOR
        self.btn_submit['fg'] = self.colors.BUTTON_BG_COLOR
        self.btn_submit['fg'] = self.colors.BUTTON_FG_COLOR
        self.left_button['bg'] = self.colors.BUTTON_BG_COLOR
        self.left_button['fg'] = self.colors.BUTTON_FG_COLOR
        self.right_button['bg'] = self.colors.BUTTON_BG_COLOR
        self.right_button['fg'] = self.colors.BUTTON_FG_COLOR
        self.up_button['bg'] = self.colors.BUTTON_BG_COLOR
        self.up_button['fg'] = self.colors.BUTTON_FG_COLOR
        self.down_button['bg'] = self.colors.BUTTON_BG_COLOR
        self.down_button['fg'] = self.colors.BUTTON_FG_COLOR


    @staticmethod
    def __get_sizes(root):
        root.update_idletasks()
        string = root.geometry()
        first_split = string.split("x")
        second_split = first_split[1].split('+')
        return int(first_split[0]), int(second_split[0])

    @classmethod
    def __place_window(cls, root):
        width, height = cls.__get_sizes(root)
        w = root.winfo_screenwidth() // 2
        h = root.winfo_screenheight() // 2
        w -= width // 2
        h -= height // 2
        root.geometry(f"+{w}+{h}")

    def refresh(self, model):
        if self.need_field_configure:
            self.__configure_field(model)
        self.result['text'] = f"Points: {model.curr_result()}"
        self.moves['text'] = f"Moves: {model.moves}"
        self.__show_random()
        for i in range(self.row_num):
            for j in range(self.col_num):
                self.__update_label(self.cells[i][j], model.get_table()[i][j])

    def __configure_field(self, model):
        self.__update_colors()
        cell_size = self.__count_cell_size()
        new_field = tk.Frame(self.main_field, bg="#ffffff", relief="ridge", borderwidth=3)
        self.cells = []
        for i in range(self.row_num):
            new_field.rowconfigure(i, weight=1)
            self.cells.append(list())
            for j in range(self.col_num):
                new_field.columnconfigure(j, weight=1)
                lbl_frame = tk.Frame(new_field, width=cell_size, height=cell_size)
                label = self.__make_label(model.get_table()[i][j], lbl_frame)
                self.cells[i].append(label)
                label.pack(fill=tk.BOTH, expand=True)
                lbl_frame.pack_propagate(False)
                lbl_frame.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
        self.field.grid_forget()
        self.field = new_field
        new_field.grid(column=0, row=0, sticky="nsew")
        self.__place_window(self.window)
        self.window.deiconify()
        self.need_field_configure = False

    def __count_cell_size(self):
        ans1 = (self.window.winfo_screenwidth() - 600) // self.col_num
        ans2 = (self.window.winfo_screenheight() - 400) // self.row_num
        return min(ans1, ans2)

    def start_loop(self, controller):
        self.controller = controller
        self.__bind_buttons()
        self.window.focus()
        self.window.mainloop()

    def __send_move(self, event, flag):
        self.controller.handle_the_move(flag)

    def __bind_buttons(self):
        self.undo_butt["command"] = self.controller.undo_move
        self.restart_butt["command"] = self.__ask_to_restart
        self.exit_butt["command"] = self.__ask_to_quit
        self.window.bind("<KeyPress>", lambda e: self.__handle_wrong_input(e))
        self.window.bind("<KeyPress-Up>", lambda e: self.__send_move(e, "w"))
        self.window.bind("w", lambda e: self.__send_move(e, "w"))
        self.window.bind("<KeyPress-Left>", lambda e: self.__send_move(e, "a"))
        self.window.bind("a", lambda e: self.__send_move(e, "a"))
        self.window.bind("<KeyPress-Down>", lambda e: self.__send_move(e, "s"))
        self.window.bind("s", lambda e: self.__send_move(e, "s"))
        self.window.bind("<KeyPress-Right>", lambda e: self.__send_move(e, "d"))
        self.window.bind("d", lambda e: self.__send_move(e, "d"))

    def __ask_to_restart(self):
        flag = askyesno(title='', message="Would you like to start a new game?")
        if flag:
            self.controller.restart_game()

    def __ask_to_quit(self):
        flag = askyesno(title='', message="Quit the game? Your progress will be lost!")
        if flag:
            self.controller.quit()

    def __make_label(self, value, parent):
        label = tk.Button(parent, borderwidth=4, relief="ridge", font=("Times New Roman", 20))
        self.__update_label(label, value)
        return label

    def __update_label(self, label, value):
        number = str(value.val)
        if value.is_empty():
            number = ''
        fg_color, bg_color, act_fg_color, act_bg_color = self.colors.choose_color(value.val)
        label.config(
            text=number,
            command=lambda: self.__label_pressed(value.val),
            foreground=fg_color,
            background=bg_color,
            activeforeground=act_fg_color,
            activebackground=act_bg_color
        )

    def __label_pressed(self, num):
        self.messages['text'] = ''
        x = random.random()
        if x <= BUTTON_PRESS_MESSAGE_CHANCE:
            elem = random.choice(BUTTON_PRESS_MESSAGES)
            if "This number is " in elem:
                if num == 0:
                    self.messages['text'] = "There is nothing!"
                else:
                    self.messages['text'] = elem + str(num)
                return
            self.messages['text'] = elem

    def __show_random(self):
        self.messages['text'] = ''
        x = random.random()
        if x <= RANDOM_COMMENT_CHANCE:
            elem = random.choice(RANDOM_COMMENTS)
            self.messages['text'] = elem

    def __handle_wrong_input(self, event):
        self.wrong_input()

    def handle_win(self, model):
        self.messages["text"] = f"CONGRATULATIONS!!! YOU WON! Your result is {model.curr_result()}"
        return askyesno(title='', message="Would you like to continue this game or start a new one?")

    def handle_loss(self, model):
        self.messages["text"] = f"Out of moves! You lost! Your result is {model.curr_result()}"
        return askyesno(title='', message="Would you like to start a new game?")

    def wrong_input(self):
        self.messages['text'] = ''
        x = random.random()
        if x <= WRONG_INPUT_REPORT_CHANCE:
            elem = random.choice(WRONG_INPUT_REPORTS)
            self.messages['text'] = elem

    def activate(self):
        while True:
            self.left_button.invoke()
            self.window.update()
            self.down_button.invoke()
            self.window.update()
            self.right_button.invoke()
            self.window.update()
            self.up_button.invoke()
            self.window.update()


class Music:
    def __init__(self, spec):
        pygame.mixer.init()

        arr = list()
        if spec == "OFF":
            pygame.mixer.music.stop()
            return
        if spec == "Minecraft":
            arr = MINECRAFT_MUSIC
        elif spec == "Beethoven":
            arr = BEETHOVEN_MUSIC
        elif spec == "Chopin":
            arr = CHOPIN_MUSIC
        song = random.choice(arr)

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(0)
