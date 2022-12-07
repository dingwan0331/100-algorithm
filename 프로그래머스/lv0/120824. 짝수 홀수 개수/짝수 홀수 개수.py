def solution(num_list):
    answer = 0
    for i in num_list:
        if i % 2 == 0:
            answer += 1
    return [answer , len(num_list)-answer]