def solution(array, n):
    array1 = list(map(lambda x: (x,abs(x-n)), array))
    answer = array1[0][0], array1[0][1]
    
    for i,j in array1:
        if j < answer[1]:
            answer = i,j
        elif j == answer[1]:
            if answer[0] > i:
                answer = i,j
            else:
                continue
    return answer[0]