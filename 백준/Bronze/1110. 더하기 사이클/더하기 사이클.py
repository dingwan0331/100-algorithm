N = int(input())
if N < 10:
    a = [0,N]
else:
    a = [ N//10 , N%10 ]

b = 0
while True:
    b += 1
    if a[1]*10 + sum(a)%10 == N:
        print(b)
        break
    else:
        a[0],a[1] = a[1] ,sum(a)%10