import tkinter
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter.messagebox import askyesno
from View import *


class Window:
    def __init__(self):
        self.controller = None
        self.row_num = 0
        self.col_num = 0

        self.window = tk.Tk()
        self.window.withdraw()
        self.window.title("2048 Game")
        self.window["bg"] = "#f4ecca"

        self.dialog = tk.Toplevel()
        self.dialog.withdraw()
        self.dialog.title("Choose settings")
        self.__dialog_init()

        self.stats = tk.Frame(self.window, bg="#f4ecca")
        self.result = tk.Label(self.stats, text='', bg="#7ad4f7", height=2)
        self.result.pack(side=tk.LEFT)
        self.moves = tk.Label(self.stats, text='', bg="#7ad4f7", height=2)
        self.moves.pack(side=tk.RIGHT)
        self.stats.pack(fill=tk.X, side=tk.TOP, padx=5, pady=(10, 5))

        self.field = tk.Frame(self.window, bg="#ffffff", relief=tk.RIDGE, borderwidth=1)
        self.field.pack(fill=tk.BOTH, padx=5, expand=True)

        self.extra_butts = tk.Frame(self.window, bg="#f4ecca")
        self.extra_butts.pack(fill=tk.X, side=tk.BOTTOM, padx=5, pady=5)
        self.undo_butt = tk.Button(self.extra_butts, borderwidth=1, bg="#e5ee88", text="Undo", font=("Times New Roman", 18))
        self.undo_butt.pack(side=tk.LEFT)
        self.exit_butt = tk.Button(self.extra_butts, borderwidth=1, bg="#eeec79", text="Exit", font=("Times New Roman", 18))
        self.exit_butt.pack(side=tk.RIGHT, padx=10)
        self.restart_butt = tk.Button(self.extra_butts, borderwidth=1, bg="#eeec79", text="Restart", font=("Times New Roman", 18))
        self.restart_butt.pack(side=tk.RIGHT, padx=10)

        self.messages = tk.Label(self.window, text='', bg="#f4ecca", height=3)
        self.messages.pack(fill=tk.X, side=tk.BOTTOM, padx=5, pady=5)

    def __dialog_init(self):
        lbl_num_rows = tk.Label(self.dialog, height=2, text="Number of lines: ", font=("Times New Roman", 18))
        self.box_num_rows = Combobox(self.dialog, state="readonly", justify=tk.RIGHT, font=("Times New Roman", 16), width=3)
        self.box_num_rows['values'] = [i for i in range(4, 11)]
        self.box_num_rows.current(0)
        lbl_num_rows.grid(row=0, column=0, sticky='ew')
        self.box_num_rows.grid(row=0, column=1)

        lbl_num_cols = tk.Label(self.dialog, height=2, text="Number of columns: ", font=("Times New Roman", 18))
        self.box_num_cols = Combobox(self.dialog, state="readonly", justify=tk.RIGHT, font=("Times New Roman", 16), width=3)
        self.box_num_cols['values'] = [i for i in range(4, 11)]
        self.box_num_cols.current(0)
        lbl_num_cols.grid(row=1, column=0, pady=1, sticky='ew')
        self.box_num_cols.grid(row=1, column=1)

        btn_submit = tk.Button(self.dialog, text='OK', font=("Times New Roman", 18), command=self.__submit_changes)
        btn_submit.grid(row=2, column=1, pady=(10, 1), sticky='we')

    def ask_settings(self):
        self.__place_window(self.dialog)
        self.dialog.deiconify()
        self.dialog.mainloop()
        self.dialog.wm_protocol("WM_DELETE_WINDOW", self.__submit_changes)
        return self.row_num, self.col_num

    def __submit_changes(self):
        self.row_num = int(self.box_num_rows.get())
        self.col_num = int(self.box_num_cols.get())
        self.dialog.withdraw()
        self.dialog.quit()

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
        self.result['text'] = f"Points: {model.curr_result()}"
        self.moves['text'] = f"Moves: {model.moves}"
        self.messages['text'] = ''
        cell_size = self.__count_cell_size()
        for i in range(self.row_num):
            self.field.rowconfigure(i, weight=1, minsize=cell_size)
            for j in range(self.col_num):
                self.field.columnconfigure(j, weight=1, minsize=cell_size)
                label = self.__make_label(model.get_table()[i][j], self.field)
                label.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
        self.__place_window(self.window)
        self.window.deiconify()

    def __count_cell_size(self):
        ans1 = (self.window.winfo_screenwidth() - 100) // self.col_num
        ans2 = (self.window.winfo_screenheight() - 350) // self.row_num
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
        self.restart_butt["command"] = self.controller.restart_game
        self.exit_butt["command"] = self.controller.quit
        self.window.bind("<KeyPress-Up>", lambda e: self.__send_move(e, "w"))
        self.window.bind("w", lambda e: self.__send_move(e, "w"))
        self.window.bind("<KeyPress-Left>", lambda e: self.__send_move(e, "a"))
        self.window.bind("a", lambda e: self.__send_move(e, "a"))
        self.window.bind("<KeyPress-Down>", lambda e: self.__send_move(e, "s"))
        self.window.bind("s", lambda e: self.__send_move(e, "s"))
        self.window.bind("<KeyPress-Right>", lambda e: self.__send_move(e, "d"))
        self.window.bind("d", lambda e: self.__send_move(e, "d"))

    @staticmethod
    def __make_label(value, parent):
        if value.val == 0:
            value = ''
        return tk.Label(parent, text=str(value), font=("Times New Roman", 20))

    def handle_win(self, model):
        self.messages["text"] = f"CONGRATULATIONS!!! YOU WON! Your result is {model.curr_result()}"
        return askyesno(title='', message="Would you like to continue this game?")

    def handle_loss(self, model):
        self.messages["text"] = f"Out of moves! You lost! Your result is {model.curr_result()}"
        return askyesno(title='', message="Would you like to start new game?")

    def wrong_input(self):
        pass
