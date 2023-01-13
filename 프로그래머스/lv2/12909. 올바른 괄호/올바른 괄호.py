def solution(s):
    stack_ = []
    try:
        for i in s:
            if i == '(':
                stack_.append(i)
            else:
                stack_.pop()
        return not bool(stack_)
    except:
        return False