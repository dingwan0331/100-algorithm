class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_map = {"I":1,"X":10,"C":100,"M":1000,"V":5,"L":50,"D":500}
        answer = 0
        previous = 0 
        for i in s[::-1]:
            if symbol_map[i] >= previous:
                answer += symbol_map[i]
            else:
                answer -= symbol_map[i]
            previous = symbol_map[i]
        return answer