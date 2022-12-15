def solution(id_list, report, k):
    report_set = set(report)
    id_dict = {id: {'count':k,'report_user':[]} for id in id_list}
    
    for i in report_set:
        user, target = i.split(' ')
        id_dict[target]['count'] -= 1
        id_dict[target]['report_user'].append(user)
    
    answer = [0 for i in id_list]
    for i in id_list:
        if id_dict[i]['count'] <= 0:
            for j in id_dict[i]['report_user']:
                answer[id_list.index(j)] += 1
    return answer