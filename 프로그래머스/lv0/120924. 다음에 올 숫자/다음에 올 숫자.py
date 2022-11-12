def solution(common):
    def is_ordinal(common):
        return common[1] - common[0] == common[2] - common[1]
    
    if is_ordinal(common):
        return common[-1] + common[1] - common[0]
    else:
        a = common[1] // common[0]
        return common[-1] * a