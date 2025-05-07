class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,v in enumerate(nums[:-1]):
            for idx, value in enumerate(nums[i+1:]):
                if v + value == target:
                    return [i,idx+i+1]