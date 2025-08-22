class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # DP 테이블 초기화
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True

        # s가 비어있을 때 p의 "*" 처리
        for j in range(1, len(p) + 1):
            if p[j-1] == '*':
                # "*"는 0번 반복될 수 있으므로, 앞의 두 문자를 건너뛴 상태와 동일
                dp[0][j] = dp[0][j-2]
        
        # DP 테이블 채우기
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # p의 현재 문자가 "*"가 아닐 때
                if p[j-1] != '*':
                    # s의 현재 문자와 p의 현재 문자가 일치하거나, p가 "."일 경우
                    # 이전의 대각선(s와 p 모두 한 칸 전) 상태를 가져옴
                    if s[i-1] == p[j-1] or p[j-1] == '.':
                        dp[i][j] = dp[i-1][j-1]
                # p의 현재 문자가 "*"일 때
                else:
                    # case 1: "*"가 0번 반복되는 경우 (s[i-1]과 p[j-2] 매칭)
                    # p에서 "*"와 그 앞 문자를 무시하고 매칭
                    zero_repeat = dp[i][j-2]

                    # case 2: "*"가 1번 이상 반복되는 경우
                    # s의 현재 문자가 "*" 앞 문자와 매칭되면
                    # s의 이전 상태(s[i-1])와 p의 현재 상태(p[j-1]) 매칭
                    one_or_more_repeat = (s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j]

                    dp[i][j] = zero_repeat or one_or_more_repeat

        # 최종 결과 반환
        return dp[len(s)][len(p)]