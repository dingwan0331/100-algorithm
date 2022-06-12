N , M = map(int,input().split())
list1 = list(map(int,input().split()))
list1.sort(reverse=True)
result = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            b = list1[i]+list1[j]+list1[k]
            if b <= M:
                result = max(result ,b)
                
print(result)