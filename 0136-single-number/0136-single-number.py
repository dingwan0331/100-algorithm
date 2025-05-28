class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = {}
        for i in nums:
            if temp.get(i) is None:
                temp[i] = 1
            else:
                temp[i] += 1
        for k,v in temp.items():
            if v == 1:
                return k