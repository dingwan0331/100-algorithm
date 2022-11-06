def solution(nums):
    answer = 0
    set_nums = set(nums)
    x = range(1,200001)
    for i in x:
        if answer >= len(nums)/2:
            break
        elif i in set_nums:
            answer += 1
    return answer