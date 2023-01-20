def solution(s):
    b = s.split(' ')
    a = 0
    c = []
    for i in range(len(b)):
        if b[i] == 'Z':
            c.pop()
        else:
            c.append(int(b[i]))
    return sum(c)