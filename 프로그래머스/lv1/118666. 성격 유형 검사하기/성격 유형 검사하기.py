def solution(survey, choices):
    dict1 = {
        'R':0, 'T':0,
        'C':0, 'F':0,
        'A':0, 'N':0,
        'J':0, 'M':0
    }
    # first = {'R':0, 'T':0,}
    # second = {'C':0, 'F':0}
    # third = {'A':0, 'N':0}
    # fourth = {'J':0, 'M':0}
    
    for i in range(len(choices)):
        result = choices[i] - 4
        if result == 0:
            continue
        elif result < 0:
            dict1[survey[i][0]] += abs(result)
        else:
            dict1[survey[i][1]] += abs(result)
    
    answer = ''
    answer += 'R' if dict1['R'] >= dict1['T'] else 'T'
    answer += 'C' if dict1['C'] >= dict1['F'] else 'F'
    answer += 'J' if dict1['J'] >= dict1['M'] else 'M'
    answer += 'A' if dict1['A'] >= dict1['N'] else 'N'
    return answer