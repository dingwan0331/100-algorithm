def solution(lines):
    answer = set()
    for i in range(len(lines)-1):
        a = set(range(lines[i][0],lines[i][1]))
        for j in range(i+1,len(lines)):
            b = set(range(lines[j][0],lines[j][1]))
            answer.update(a&b)
    return len(answer)