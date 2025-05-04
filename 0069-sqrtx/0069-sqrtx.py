class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        left = 1
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            sqrt = x // mid
            if mid == sqrt:
                return int(mid)
            if mid < sqrt :
                left = mid + 1
            if mid > sqrt:
                right = mid - 1
        return int(right)