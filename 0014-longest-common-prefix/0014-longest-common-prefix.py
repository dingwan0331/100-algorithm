class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) ==1:
            return strs[0]
        result = ""
        ss = ""
        strs.sort(key=len)
        standard = strs[0]
        st_len = len(standard)
        idx = 0
        for i in range(st_len):
            ss += standard[i]
            for j,v in enumerate(strs[1:]):
                if ss != v[idx:i+1]:
                    break
                elif j == len(strs[1:]) -1 :
                    result = ss
        return result