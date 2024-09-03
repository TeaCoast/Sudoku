from dataclasses import dataclass

symbols = list("123456789")

class SudokuMatrix:
    values: list[int]

    def get_row(self, row_i: int):
        return [self.values[row_i*9 + column_i] for column_i in range(9)]
    
    def get_column(self, column_i: int):
        return [self.values[row_i*9 + column_i] for row_i in range(9)]