class Solution:
    def minMaxDifference(self,num: int) -> int:
        s = str(num)
    
        for ch in s:
            if ch != '9':
                max_version = s.replace(ch, '9')
                break
        else:
            max_version = s
    
        min_version = s.replace(s[0],"0")
    
        return int(max_version) - int(min_version)