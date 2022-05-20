A = int(input())
B = int(input())
C = int(input())
a = str(A*B*C)
for i in range(10):
    print(a.count(f'{i}'))