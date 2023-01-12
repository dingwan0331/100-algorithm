def solution(n):
    b_n = bin(n)
    b_n_0 = b_n.count('0')
    b_n_1 = b_n.count('1')
    n += 1
    while bin(n).count('0') != b_n_0 and bin(n).count('1') != b_n_1:
        n +=1            
    return n