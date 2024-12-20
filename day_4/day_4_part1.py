import os
import math

def main():
    HOME = os.path.expanduser("~")
    WDIR = "advent_2024/day_4"
    INPUT = "small_input.txt"
    WORD = "XMAS"
    matrix = Matrix(read_input_file(f"{HOME}/{WDIR}/{INPUT}"))
    count_words(WORD, matrix)


def count_words(word, matrix):
    for var in vars(word):
        pass


def read_input_file(file):
    data = []
    with open(file, "r", encoding="utf-8") as input_file:
        for line in input_file:
            data.append(line)
    return data


class Matrix:
    def __init__(self, matrix):
        self.matrix = [x.strip() for x in matrix]
        self.mirror = self._mirror(self.matrix)
        self.transpose = self._transpose(self.matrix)
        self.opposite_transpose = self._mirror(self.transpose)
        self.diagonals = self._diagonals_to_rows(self.matrix)
        self.reverse_diagonals = self.mirror(self.diagonals)

    def _mirror(self, matrix):
        mirroed_matrix = []
        for row in matrix:
            mirroed_matrix.append(row[::-1])
        return mirroed_matrix

    def _transpose(self, matrix):
        transposed_matrix = []
        row_width = len(matrix[0])
        column_height = len(matrix)
        count_column = 0
        count_row = 0
        transposed_string = ""
        while count_column < row_width:
            while count_row < column_height:
                transposed_string += self.matrix[count_row][count_column]
                count_row += 1
            transposed_matrix.append(transposed_string)
            transposed_string = ""
            count_row = 0
            count_column += 1
        return transposed_matrix
    
    def _diagonals_to_rows(self, matrix):
        diagonals = []
        row_width = len(matrix[0])
        column_height = len(matrix)
        diagonal = math.sqrt(row_width**2 + column_height**2)
        current_diagonal_length = 1
        column_index = 0
        row_index = column_height - 1
        hit_diagonal = False

        while row_index >= 0:
            diagonal_entries = []
            self._make_diagonal(row_index, column_index, current_diagonal_length, diagonal_entries) 
            diagonals.append(diagonal_entries)
            if current_diagonal_length == diagonal:
                hit_diagonal = True
                row_index -= 1
                current_diagonal_length += 1

        return diagonals

    def _make_diagonal(self, row_index, column_index, diagonal_length, diagonal_entries):

        if diagonal_length != 0:
            diagonal_entries += self.matrix[row_index][column_index]
            row_index -= 1
            column_index += 1
            diagonal_length -= 1
            self._make_diagonal(row_index, column_index,diagonal_length,diagonal_entries)
        else:
            return diagonal_entries
        


if __name__ == "__main__":
    main()
