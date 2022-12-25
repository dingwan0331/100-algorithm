from datetime import datetime

def solution(a, b):
    year = '2016'
    date = datetime.strptime(year+str(a)+str(b),'%Y%m%d')
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    day_idx = datetime.weekday(date)
    return day[(day_idx+1)%7]