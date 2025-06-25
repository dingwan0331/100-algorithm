class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                gap = nums[j] - nums[i]
                if gap >max_diff and gap > 0 :
                    max_diff = gap
        return max_diff