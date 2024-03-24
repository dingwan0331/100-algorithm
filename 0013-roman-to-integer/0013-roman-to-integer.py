class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_map = {"I":1,"X":10,"C":100,"M":1000,"V":5,"L":50,"D":500}
        answer = 0
        for i in range(len(s)):
            if i == len(s)-1:
                answer += symbol_map[s[i]]
            elif symbol_map[s[i]] >= symbol_map[s[i+1]]:
                answer += symbol_map[s[i]]
            else:
                answer -= symbol_map[s[i]]
        return answer