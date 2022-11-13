def solution(quiz):
    answer = []
    for i in quiz:
        i = i.replace('=','==')
        answer.append('O' if eval(i) else 'X')
    return answer