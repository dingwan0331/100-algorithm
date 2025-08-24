class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result, length = [], len(nums)

        for i in range(length - 2):
            # 1. 고정점 중복 제거
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, length - 1
            
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                
                if current_sum < 0:
                    l += 1
                elif current_sum > 0:
                    r -= 1
                else:
                    # 합이 0일 때
                    result.append([nums[i], nums[l], nums[r]])
                    
                    # 2. 투 포인터 중복 제거
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    # 다음 탐색을 위해 포인터 이동
                    l += 1
                    r -= 1
        return result