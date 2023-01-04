def solution(array, commands):
    answer = []
    for n in range(len(commands)):
        i = commands[n][0] - 1
        j = commands[n][1] 
        k = commands[n][2] - 1
        answer.append(sorted(array[i:j])[k])
    
    return answer