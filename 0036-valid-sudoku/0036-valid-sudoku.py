class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = {str(i): set() for i in range(1,10)}
        row = {str(i): set() for i in range(1,10)}
        space = {str(i): set() for i in range(1,10)}
        for i,v in enumerate(board):
            for idx,value in enumerate(v):
                if self.check_duplicate(i,idx,value,col,row,space) == False:
                    return False
        return True

                
    
    def check_duplicate(self,idx1:int,idx2:int,value:str,col,row,space)-> bool:

        row_num = idx2//3 + 1
        col_num = idx1//3 + 1
        space_idx = (col_num -1) *3 + row_num
        if value == ".":
            return True
        else:
            print(space_idx)
            if value in row[str(idx2+1)]:
                print(1)
                return False
            if value in col[str(idx1+1)]:
                print(2)
                return False
            if value in space[str(space_idx)]:
                
                print(3)
                return False
        row[str(idx2+1)].add(value)
        col[str(idx1+1)].add(value)
        space[str(space_idx)].add(value)
        return True