def solution(s):
    answer = ''
    j = 0
    for i in range(len(s)):
        if s[i]==' ':
            answer += ' '
            j=-1
        elif j%2 == 0:
            answer += s[i].upper()
        else:
            answer += s[i].lower()
        j+=1
    return answer