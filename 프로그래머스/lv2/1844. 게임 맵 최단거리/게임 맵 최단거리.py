from collections import deque

def solution(maps):
    m = len(maps[0]) -1
    n = len(maps) -1
    
    
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    start = [0,0]
    
    queue = deque([start])
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or ny > m or nx > n:
                continue
            
            if maps[nx][ny] == 0:
                continue
                
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append([nx,ny])
    
    return maps[n][m] if maps[n][m] != 1 else -1