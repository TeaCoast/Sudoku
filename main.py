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
    
    def num_to_str(self, num: int):
        if num == 0:
            return ' '
        return str(num)

    def __str__(self) -> str:
        lines = []
        for row_block_i in range(3):
            for row_i in range(3):
                row = []
                for column_block_i in range(3):
                    row.append('')
                    for column_i in range(3):
                        row[-1] += ' ' + self.num_to_str(self.get_value_from_block(row_block_i, row_i, column_block_i, column_i)) + ' '
                lines.append('|'.join(row))
            if row_block_i < 2:
                lines.append("-" * len(lines[-1]))
        return '\n'.join(lines)
    
@dataclass
class SudokuNoteMatrix:
    domains: list[set[int]]

    def get_value(self, row_i: int, column_i: int):
        return self.domains[row_i * 9 + column_i]
    
    def get_value_from_block(self, row_block_i: int, row_i: int, column_block_i: int, column_i: int):
        return self.get_value(row_block_i*3 + row_i, column_block_i*3 + column_i)
    
    def get_note_from_block(self, row_block_i: int, row_i: int, row_note_i: int, column_block_i: int, column_i: int, column_note_i: int):
        return list(self.get_value(row_block_i*3 + row_i, column_block_i*3 + column_i))[row_note_i*3 + column_note_i]

    def get_row(self, row_i: int) -> list[int]:
        return [self.get_value(row_i, column_i) for column_i in range(9)]
    
    def get_column(self, column_i: int) -> list[int]:
        return [self.get_value(row_i, column_i) for row_i in range(9)]
    
    def get_block(self, row_block_i: int, column_block_i: int) -> list[int]:
        return [self.get_value_from_block(row_block_i, row_i, column_block_i, column_i) 
                for column_i in range(3) for row_i in range(3)]
    
    def num_to_str(self, num: int):
        if num == 0:
            return ' '
        return str(num)

    def __str__(self) -> str:
        lines = []
        # columns
        for row_block_i in range(3):
            lines.append([])
            for row_i in range(3):
                lines[row_block_i].append([])
                for row_note_i in range(3):
                    # columns
                    lines[row_block_i][row_i].append([])
                    for column_block_i in range(3):
                        lines[row_block_i][row_i][row_note_i].append([])
                        for column_i in range(3):
                            lines[row_block_i][row_i][row_note_i][column_block_i].append([])
                            for column_note_i in range(3):
                                lines[row_block_i][row_i][row_note_i][column_block_i][column_i].append([])
                                lines[row_block_i][row_i][row_note_i][column_block_i][column_i][column_note_i] = self.num_to_str(self.get_note_from_block(
                                      row_block_i, row_i, row_note_i, column_block_i, column_i, column_note_i
                                ))
        length = len("7  8  9 | 7  8  9 | 7  8  9 || 7  8  9 | 7  8  9 | 7  8  9 || 7  8  9 | 7  8  9 | 7  8  9")
        return ('\n' + '='*length + '\n').join(
                    ('\n' + '-'*length + '\n').join(
                        ('\n').join(
                            (' || ').join(
                                (" | ").join(
                                    ("  ").join(
                                        ("").join(column_note for column_note in column) 
                                    ) for column in column_block
                                ) for column_block in row_note
                            ) for row_note in row
                        ) for row in row_block
                    ) for row_block in lines
                )


sudoku_matrix = SudokuNoteMatrix([{1, 2, 3, 4, 5, 6, 7, 8, 9}] * 81)

print(sudoku_matrix)