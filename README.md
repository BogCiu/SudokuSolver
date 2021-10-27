# SudokuSolver
Sudoku solver in python

SudokuEnterGenerator.py creates a drawn Sudoku board in an excel file named SudokuExcel.xlsx
SudokuBruteForceTraceback.py takes the SudokuExcel.xlsx file and starts BruteForce solving the puzzle:
  -Empty cells are completed with digits starting from 1 to 9.
  -After each completion, the puzzle is checked for validity (if rules of sudoku are broken) or finished status (if all the values in the cell are less then 10)
  -Default values of the cells are: Row coordonate * 10 + Column (this is needed because the default non-valid values have to all be unique to verify validity)
  -Validity is checked by checking of the length of the list of all elements in a row/column/square is the same as the length of the set formed by the same elements)
  
Because the "finish" condition described above does **NOT** imply validity of the puzzle, the solving algorithm will keep running as long as the puzzle is **NOT** finished **OR** **NOT** valid
