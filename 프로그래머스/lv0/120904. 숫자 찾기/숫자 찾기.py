def solution(num, k):
    try:
        list1 = list(map(int,str(num)))
        return list1.index(k) +1
    except:
        return -1