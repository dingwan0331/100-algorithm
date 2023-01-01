def solution(x):
    x_list = list(map(int,str(x)))
    sum_x = sum(x_list)
    return bool(x % sum_x) == False