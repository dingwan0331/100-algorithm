class Solution:
    def longestPalindrome(self,s):
        if len(s) < 2:
            return s

        start = 0
        max_length = 1
    
        for i in range(len(s) - 1):
            left1, right1 = self.expand_around_center(i, i,s)      # odd length palindrome
            if right1 - left1 + 1 > max_length:
                start = left1
                max_length = right1 - left1 + 1

            left2, right2 = self.expand_around_center(i, i + 1,s)  # even length palindrome
            if right2 - left2 + 1 > max_length:
                start = left2
                max_length = right2 - left2 + 1

        return s[start:start + max_length]

    def expand_around_center(self,left, right,s):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1