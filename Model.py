import random
from Inner_Settings import *


class SizeError(Exception):
    pass


class Cell:
    def __init__(self, row, col, value=0):
        self.__value = value
        self.__row = row
        self.__col = col

    @property
    def val(self):
        return self.__value

    @val.setter
    def val(self, value):
        self.__value = value

    def __str__(self):
        if self.is_empty():
            return '*'
        return str(self.val)

    def __eq__(self, other):
        return self.val == other.val

    def is_empty(self):
        return self.val == 0

    def get_coords(self):
        return self.__row, self.__col

    def merge(self, other):
        if self != other or self.get_coords() == other.get_coords():
            return None
        self.val = 0
        other.val *= 2
        return other.val

    def swap(self, other):
        self.val, other.val = other.val, self.val


class Field:
    MIN_SIZE = MIN_SIZE_VALUE
    MAX_SIZE = MAX_SIZE_VALUE
    WIN_CELL = WIN_SELL_VALUE

    def __init__(self, rows=4, cols=4):
        self.__check_size(rows, cols)
        self.height = rows
        self.width = cols
        self.__win = False
        self.__table = list()
        self.__empties = {i for i in range(rows * cols)}
        self.__result = 0
        self.__moves = 0
        self.__generate_field()

    @property
    def moves(self):
        return self.__moves

    @classmethod
    def __check_size(cls, height, width):
        if not all(cls.MIN_SIZE <= x <= cls.MAX_SIZE for x in [height, width]):
            raise SizeError()

    def __generate_field(self):
        for i in range(self.height):
            row = [Cell(i, j) for j in range(self.width)]
            self.__table.append(row)
        for _ in range(2):
            self.__fill_random()

    def __fill_random(self):
        if not self.__empties:
            return
        new_val = 2
        x = random.random()
        if x >= 0.9:
            new_val = 4
        ind = random.choice(list(self.__empties))
        row, col = self.__get_coords(ind)
        self.__table[row][col].val = new_val
        self.__empties.remove(ind)

    def __get_coords(self, ind):
        return ind // self.width, ind % self.width

    def __get_ind(self, row, col):
        return row * self.width + col

    def curr_result(self):
        return self.__result

    def check_win(self):
        return self.__win

    def get_table(self):
        return self.__table

    def is_lost(self):
        if self.__empties:
            return False
        table = self.get_table()
        for i in range(self.height - 1):
            for j in range(self.width - 1):
                if table[i][j] == table[i + 1][j] or table[i][j] == table[i][j + 1]:
                    return False
            if table[i][self.width - 1] == table[i + 1][self.width - 1]:
                return False
        for j in range(self.width - 1):
            if table[self.height - 1][j] == table[self.height - 1][j + 1]:
                return False
        return True

    def move(self, flag):
        self.__empties = set()
        rows = self.__select_rows(flag)
        is_changed = False
        for elem in rows:
            is_changed = self.__move_cells(elem) or is_changed
        if is_changed:
            self.__moves += 1
            self.__fill_random()
        return is_changed


    def __select_rows(self, flag):
        if flag == 'd':
            return [row for row in self.__table]
        if flag == 'a':
            return [row[::-1] for row in self.__table]
        if flag == 's':
            return [[self.__table[i][j] for i in range(self.height)] for j in range(self.width)]
        if flag == 'w':
            return [elem[::-1] for elem in self.__select_rows('s')]

    def __move_cells(self, arr):
        is_moved = False
        length = len(arr)
        j = length
        i = j - 1
        while arr[i].is_empty():
            i -= 1
            if i == -1:
                for elem in arr:
                    ind = self.__get_ind(*elem.get_coords())
                    self.__empties.add(ind)
                return is_moved
        j -= 1
        while i >= 0:
            if arr[i].is_empty() or i == j:
                i -= 1
                continue
            merge_try = arr[i].merge(arr[j])
            if merge_try is None:
                if arr[j].is_empty():
                    arr[i].swap(arr[j])
                    is_moved = True
                else:
                    arr[i].swap(arr[j - 1])
                    is_moved = is_moved or (i != j - 1)
                    j -= 1
            else:
                self.__result += merge_try
                self.__win = (merge_try == self.WIN_CELL) or self.__win
                j -= 1
                is_moved = True
            i -= 1
        if arr[j].is_empty():
            ind = self.__get_ind(*arr[j].get_coords())
            self.__empties.add(ind)
        for k in range(j):
            ind = self.__get_ind(*arr[k].get_coords())
            self.__empties.add(ind)
        return is_moved
