from collections import deque

def solution(m, n, puddles):
    
    distances = []
    dx = [0, 1] ## 가로
    dy = [1, 0] ## 세로
    
    queue = deque([(1,1,0)]) ## (x좌표, y좌표, 이동한 칸의 위치)
    while queue:
        x, y, dis = queue.popleft()
        
        if x==m and y==n:
            distances.append(dis)
        
        for i in range(2):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx > 0 and nx <= m and ny > 0 and ny <= n and [nx, ny] not in puddles:
                queue.append((nx, ny, dis+1))
        
    answer = distances.count(min(distances))
    return answer % 1000000007

if __name__ == '__main__':
    print(solution(4, 3, [[2, 2]]))