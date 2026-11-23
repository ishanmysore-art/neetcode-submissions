class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                entry = board[r][c]

                if entry == ".":
                    continue
                
                b = r // 3 * 3 + c // 3

                if entry in rows[r] or entry in cols[c] or entry in boxes[b]:
                    return False
                
                rows[r].add(entry)
                cols[c].add(entry)
                boxes[b].add(entry)
        
        return True
                
