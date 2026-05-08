class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows 
        n = len(board[0])
        for i in range(n):
            count = set()
            for j in range(n):
                if board[i][j] in count:
                    print(f"false, row, value {board[i][j]}")
                    return False
                if board[i][j] != ".":
                    count.add(board[i][j])
        for i in range(n):
            count = set()
            for j in range(n):
                if board[j][i] in count:
                    print(f"false, col, value {board[j][i]}")
                    return False 
                if board[j][i] != ".":
                    count.add(board[j][i])
        for m in range(0,n,3):  
            for l in range(0,n,3):
                count = set()
                for i in range(m,m+3):
                    print(count)
                    for j in range(l,l+3):
                        if board[i][j] in count:
                            print(count)
                            print(f"false, box, row: {i}, col: {j}, board:{board[i][j]}")
                            return False 
                        if board[i][j] != ".":
                            count.add(board[i][j])
        # check columns 
        # check 3x3 sub-boxes
        return True