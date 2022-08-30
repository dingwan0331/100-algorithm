# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/12930?language=python3

def solution(str):
  answer = ''
  count = 0
  for i in str:
    if i == ' ':
      answer += ' '
      count = 0
      continue
    answer += i.upper() if count % 2 == 0 else i.lower()
    count += 1
  return answer