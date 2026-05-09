class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows 
        n = len(board[0])
        for i in range(n):
            count = set()
            for j in range(n):
                if board[i][j] in count:
                    return False
                if board[i][j] != ".":
                    count.add(board[i][j])
        for i in range(n):
            count = set()
            for j in range(n):
                if board[j][i] in count:
                    return False 
                if board[j][i] != ".":
                    count.add(board[j][i])
        for square in range(n):  
            count = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3)*3+i
                    col = (square % 3)*3+j
                    if board[row][col] in count:
                        return False 
                    if board[row][col] != ".":
                        count.add(board[row][col])
        # check columns 
        # check 3x3 sub-boxes
        return True