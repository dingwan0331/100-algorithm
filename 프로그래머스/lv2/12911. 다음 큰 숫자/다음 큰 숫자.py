def solution(n):
    b_n = bin(n)
    b_n_1 = b_n.count('1')
    n += 1
    while bin(n).count('1') != b_n_1:
        n +=1            
    return n