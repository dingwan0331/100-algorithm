N = int(input())
b = list(map(int,input().split()))
a = 0
for i in range(len(b)):
    a += b[i]/max(b)*100
    
print(a/N)