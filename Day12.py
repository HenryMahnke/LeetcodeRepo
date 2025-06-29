"""
Valid Sodoku
given a 9x9 sudoku board "board".
Rules 
each row must contain the digits 1-9 wihtout duplicates 
each column must containt he digits 1-9 without duplicates 
each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 wihtout duplicates

board does not need to be full or be solvable to be valid 
Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
 input format

 time com;olexity O(n^2) time, O(n^2) - added space
"""
def isValidSudoku(board): 
    #check the rows
    for row in board: 
        rowHash ={}
        for elemInRow in row: 
            curVal= rowHash.get(elemInRow, 0)
            if elemInRow == '.':
                continue
            if curVal != 0 or not int(elemInRow) <10 or not int(elemInRow) > 0: 
                return False 
            else: 
                # print(elemInRow)
                rowHash[elemInRow] = curVal + 1
    #check the columns
    transposed_array = [list(row) for row in zip(*board)]    
    #check the cols  
    for col in transposed_array:
        colHash ={}
        for elemInCol in col: 
            curVal= colHash.get(elemInCol, 0)
            if elemInCol == ".":
                continue
            if curVal != 0 or not int(elemInCol) <10 or not int(elemInCol) > 0: 
                return False 
            else: 
                colHash[elemInCol] = curVal + 1
    #now check the boxes 
    #tempted to flatten the board ^^ would make above operations better 
    flattened = []
    for row in board: 
        flattened.extend(row)
        #maybe need *
    for curBoxRow in range(3):
        for curBoxCol in range(3):
            boxHash = {}
            boxStart = 27 * curBoxRow + 3*curBoxCol
            # print(boxStart)
            for i in range(3): 
                for j in range(3): 
                    curEl = flattened[boxStart+9*i+j]
                    curVal  = boxHash.get(curEl,0) 
                    if curEl == ".": 
                        continue
                    if curVal != 0: 
                        return False
                    boxHash[curEl] = curVal + 1
    return True
                



board = [
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
]
print(isValidSudoku(board)) 