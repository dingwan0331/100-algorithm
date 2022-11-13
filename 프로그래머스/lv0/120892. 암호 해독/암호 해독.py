def solution(cipher, code):
    N = len(cipher)
    idx = code-1
    idx_list = []
    
    while N > idx:
        idx_list.append(idx)
        idx += code
        
    answer = ''
    for i in idx_list:
        answer += cipher[i]
    return answer