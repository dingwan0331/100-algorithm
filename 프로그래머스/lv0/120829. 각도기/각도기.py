def solution(angle):
    if angle == 180:
        return 4
    if angle > 90:
        return 3
    return angle//90+1