import sys
N = int(input())
a = [sys.stdin.readline() for i in range(N)]
for i in range(N):
    n = 0
    t = []
    for j in a[i]:
        if j == "O":
            n += 1
            t.append(n)
        else:
            n = 0
            t.append(n)
    print(sum(t))