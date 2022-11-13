def solution(board):
    dx = [-1,1,0,0,1,1,-1,-1]
    dy = [0,0,1,-1,1,-1,1,-1]
    
    N = len(board)
    answer = [[1 for i in range(N)]for i in range(N)]
    def a(x,y):
        answer[x][y] = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue
            answer[nx][ny] = 0
        return 
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                a(i,j) 
    
    result = 0 
    
    for i in range(N):
        result += sum(answer[i])

    return result
            