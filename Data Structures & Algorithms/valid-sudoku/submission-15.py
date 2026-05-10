class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows 
        n = len(board[0])
        # for i in range(n):
        #     count = set()
        #     for j in range(n):
        #         if board[i][j] in count:
        #             return False
        #         if board[i][j] != ".":
        #             count.add(board[i][j])
        # for i in range(n):
        #     count = set()
        #     for j in range(n):
        #         if board[j][i] in count:
        #             return False 
        #         if board[j][i] != ".":
        #             count.add(board[j][i])
        count = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)
        for r in range(n):
            for c  in range(n):
                if board[r][c] ==".":
                    continue 
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or 
                board[r][c] in count[(r//3,c//3)]):
                    return False 
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                count[(r//3,c//3)].add(board[r][c])
        # check columns 
        # check 3x3 sub-boxes
        return True