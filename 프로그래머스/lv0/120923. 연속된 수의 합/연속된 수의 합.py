def solution(num, total):
    half = num // 2
    mid = total // num
    if num % 2:
        return [i for i in range(mid- half, half+mid+1)]
    else:
        return [i for i in range(mid+1  -half, half+mid+1)]