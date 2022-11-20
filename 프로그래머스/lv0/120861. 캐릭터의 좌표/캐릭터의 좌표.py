def solution(keyinput, board):
    directions = {
        'up':(0,1),
        'down':(0,-1),
        'left':(-1,0),
        'right':(1,0)
    }
    n, m = board[0], board[1]
    now = (0,0)
    
    for key in keyinput:
        target = (directions[key][0] + now[0], directions[key][1] + now[1])
        if abs(target[0]) > n//2 or abs(target[1]) > m//2:
            continue
        else:
            now = target
    return now