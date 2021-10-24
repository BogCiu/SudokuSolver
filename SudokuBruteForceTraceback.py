import openpyxl as xl
import numpy
import SudokuCheckFunctions as check

is_valid = False
is_finished = True


class SudokuCell:
    is_given = None
    last_attempted_value = 0

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.current_value = (row * 10 + column)


c = numpy.empty((9, 9), dtype=object)

wb = xl.open("SudokuExcel.xlsx")
ws = wb['Sheet']

for row in range(1, 10):
    for column in range(1, 10):
        c[row - 1][column - 1] = SudokuCell(row, column)
        if ws.cell(row, column).value:
            c[row - 1][column - 1].is_given = False
            c[row - 1][column - 1].current_value = ws.cell(row, column).value
        else:
            c[row - 1][column - 1].is_given = True

wb.save("SudokuExcelSolved.xlsx")

is_valid = check.check_validity(c)
print(f'Puzzle validity is {is_valid}')

is_finished = check.check_finished(c)
print(f'Puzzle finished status is {is_finished}')
# for i in range(0,9):
#    for j in range(0,9):
#        print(c[i][j].current_value, end =" ")
#    print('\n')
