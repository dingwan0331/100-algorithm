def solution(n):
    answer = 0
    for i in range(1,n+1):
        a = []
        for j in range(i,n+1):
            a.append(j)
            if sum(a) == n:
                answer += 1
                break
            if sum(a) > n:
                break
    return answer