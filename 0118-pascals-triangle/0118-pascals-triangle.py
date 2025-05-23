class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1],[1,1]]
        for i in range(2,numRows):
            temp = result[-1]
            temp_list = [1]
            for j in range(len(temp)-1):
                temp_list.append(temp[j]+temp[j+1])
            temp_list.append(1)
            result.append(temp_list)
        if numRows ==1:
            result.pop()
            return result
        return result
                
