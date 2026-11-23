class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_row, hash_col, hash_box = {}, {}, {}
        for row in range(len(board)):
            for col in range(len(board[row])):
                entry = board[row][col]
                box_index = row // 3 * 3 + col // 3

                if entry != ".":
                    entry = int(entry)
                    if row in hash_row and entry in hash_row[row]:
                        #print("oh no row")
                        return False
                    #print("Box index: ", box_index)
                    #print("Entry: ", entry)
                    if box_index in hash_box and entry in hash_box[box_index]:
                        #print("oh no box")
                        return False
                    
                    if row not in hash_row:
                        hash_row[row] = {}
                    hash_row[row][entry] = 1

                    if box_index not in hash_box:
                        hash_box[box_index] = {}
                    hash_box[box_index][entry] = 1

                if entry != ".":
                    entry = int(entry)
                    if col in hash_col and entry in hash_col[col]:
                        #print("oh no col")
                        return False
                    if col not in hash_col:
                        hash_col[col] = {}
                    hash_col[col][entry] = 1
        return True