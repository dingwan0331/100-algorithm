def solution(emergency):
    list1 = sorted(emergency, reverse=True)
    return list(map(lambda x : list1.index(x)+1, emergency))