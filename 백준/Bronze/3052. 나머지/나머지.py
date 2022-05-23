a = []
b = []
while True:
    try:
        a.append(int(input()))
    except:
        break
for i in range(len(a)):
    b.append(a[i]%42)
    
print(len(set(b)))