class Solution:
    def generateParenthesis(self, n):
        result = []
    
        def backtrack(s, open, close):
            # 괄호 n쌍을 모두 사용했다면 완성
            if len(s) == 2 * n:
                result.append(s)
                return
    
            # '(' 추가
            if open < n:
                backtrack(s + "(", open + 1, close)
    
            # ')' 추가
            if close < open:
                backtrack(s + ")", open, close + 1)
    
        backtrack("", 0, 0)
    
        return result