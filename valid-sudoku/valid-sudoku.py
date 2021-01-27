class Solution(object):
    def isValidSudoku(self, board):
        #We can break it up into three separate checks.
        
        #First: Rows
        for i in range(len(board)):
            row = "".join([e for e in board[i] if e != "."])
            if len(set(row)) != len(row): return False
            
        #Second: Columns
        for i in range(len(board[0])):
            col = "".join([e[i] for e in board if e[i] != "."])
            if len(set(col)) != len(col): return False
            
        #Third: 3x3 Sub-Boxes
        for i in range(3):
            for j in range(3):
                boxArr = [board[i*3][j*3], board[i*3][j*3+1], board[i*3][j*3+2], board[i*3+1][j*3], 
                          board[i*3+2][j*3], board[i*3+1][j*3+1], board[i*3+1][j*3+2], 
                          board[i*3+2][j*3+1], board[i*3+2][j*3+2]]
                box = "".join([e for e in boxArr if e != "."])
                if len(set(box)) != len(box): return False
        return True
