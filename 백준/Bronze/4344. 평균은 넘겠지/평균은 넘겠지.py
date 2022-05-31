import sys
a = []
C = int(input())
for i in range(C):
    a.append(list(map(int,sys.stdin.readline().split())))
for i in range(C):
    a[i].pop(0)
    b = sum(a[i]) / (len(a[i]))
    rea = 0
    for j in a[i]:
        if j > b:
            rea += 1
    pr = round(rea / len(a[i]),5)*100
    print('%.3f'% pr,'%',sep="")