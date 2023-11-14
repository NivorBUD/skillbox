from typing import List


class Matrix:
    def __init__(self, rows, columns, data: list[list[int]] = None):
        self.rows = rows
        self.columns = columns
        self.data = data

    def checkSizesToAddSub(self, other):
        return isinstance(other, Matrix) and self.rows == other.rows and self.columns == other.columns

    def __add__(self, other):
        if self.checkSizesToAddSub(other):
            return Matrix(self.rows, self.columns,
                          [[self.data[row][column] + other.data[row][column] for column in range(self.columns)]
                           for row in range(self.rows)])

    def __sub__(self, other):
        if self.checkSizesToAddSub(other):
            return Matrix(self.rows, self.columns,
                          [[self.data[row][column] - other.data[row][column] for column in range(self.columns)]
                           for row in range(self.rows)])

    def checkToMult(self, other):
        return isinstance(other, Matrix) and self.rows == other.columns

    def __mul__(self, other):
        if self.checkToMult(other):
            return Matrix(self.rows, other.columns,
                          [[sum(self.data[n_row][swap_index] * other.data[swap_index][n_col]
                                for swap_index in range(self.columns))
                            for n_col in range(other.columns)] for n_row in range(self.rows)])

    def transpose(self):
        return Matrix(self.columns, self.rows,
                      [[self.data[row][column] for row in range(self.rows)] for column in range(self.columns)])

    def __str__(self):
        res = ''
        for row in range(self.rows):
            for column in range(self.columns):
                res += ' ' + str(self.data[row][column])
            res += '\n'
        return res
        return '\n'.join(' '.join())
