class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        length = len(nums)
        idxs = []
        for i in range(length):
            if nums[i] == key:
                idxs.append(i)
        result = []
        for i in idxs:
            max_index = min(i+k+1,length)
            min_index = i-k
            for j in range(min_index,max_index):
                if j >=0:
                    result.append(j)

        return list(set(result))