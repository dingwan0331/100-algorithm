from collections import deque

def solution(my_string):
    q = deque(my_string)
    new_set = set()
    answer = ''
    while q:
        i = q.popleft()
        if i not in new_set:
            answer += i
            new_set.add(i)
            
    return answer