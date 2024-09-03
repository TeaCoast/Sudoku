from dataclasses import dataclass

symbols = list("123456789")

@dataclass
class SudokuMatrix:
    values: list[int]

    def get_value(self, row_i: int, column_i: int):
        return self.values[row_i * 9 + column_i]
    
    def get_value_from_block(self, row_block_i: int, row_i: int, column_block_i: int, column_i: int):
        return self.get_value(row_block_i*3 + row_i, column_block_i*3 + column_i)

    def get_row(self, row_i: int) -> list[int]:
        return [self.get_value(row_i, column_i) for column_i in range(9)]
    
    def get_column(self, column_i: int) -> list[int]:
        return [self.get_value(row_i, column_i) for row_i in range(9)]
    
    def get_block(self, row_block_i: int, column_block_i: int) -> list[int]:
        return [self.get_value_from_block(row_block_i, row_i, column_block_i, column_i) 
                for column_i in range(3) for row_i in range(3)]
    
    def __str__(self) -> str:
        lines = []
        for row_block_i in range(3):
            for row_i in range(3):
                row = []
                for column_block_i in range(3):
                    row.append('')
                    for column_i in range(3):
                        row[-1] += ' ' + str(self.get_value_from_block(row_block_i, row_i, column_block_i, column_i)) + ' '
                lines.append('|'.join(row))
            if row_block_i < 2:
                lines.append("-" * len(lines[-1]))
        return '\n'.join(lines)
    
    def are_requirements_met(self) -> bool:
        def add_requirement(requirement: bool):
            if requirement == False:
                raise ValueError
        try:
            for row_i in range(9):
                row = self.get_row(row_i)
                for i in range(1, 10):
                    add_requirement(row.count(i) == 1)
            for column_i in range(9):
                column = self.get_column(column_i)
                for i in range(1, 10):
                    add_requirement(column.count(i) == 1)
            for row_block_i in range(3):
                for column_block_i in range(3):
                    block = self.get_block(row_block_i, column_block_i)
                    for i in range(1, 10):
                        add_requirement(block.count(i) == 1)
        except ValueError:
            return False
        return True



    

sudoku_matrix = SudokuMatrix([(row_i + column_i) % 9 + 1 for column_i in range(9) for row_i in range(9)])

print(sudoku_matrix.are_requirements_met())
