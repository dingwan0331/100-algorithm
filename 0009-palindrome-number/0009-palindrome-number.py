class Solution:
    def isPalindrome(self, x: int) -> bool:
        base = str(x)
        compare = base[::-1]
        return base == compare