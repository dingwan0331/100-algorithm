from datetime import datetime

def solution(a, b):
    date = '2016'+str(a)+str(b)
    date = datetime.strptime(date,'%Y%m%d')
    week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    day_idx = (datetime.weekday(date)+1 ) % 7
    return week[day_idx]