class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = 0
        
        for i in range(n):
            next_i = (i + 1) % n  # 원형 배열 처리
            diff = abs(nums[i] - nums[next_i])
            max_diff = max(max_diff, diff)
        
        return max_diff