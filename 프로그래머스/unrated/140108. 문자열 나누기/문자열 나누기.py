def solution(s):
    def my_func(s,answer):
        x,y = 0,0
        x_str = s[0]
        for i in range(len(s)):
            if i != 0 and x == y:
                return s[i:], answer +1
            if s[i] == x_str:
                x += 1
            else:
                y += 1
        return False, answer +1
    answer = 0
    while s:
        s, answer = my_func(s,answer)
    return answer