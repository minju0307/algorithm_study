from collections import deque

def solution(maps):
    n = len(maps)-1
    m = len(maps[0])-1
    
    dx = [0, 0, 1, -1] ## 동, 서, 남, 북 (상하 움직임)
    dy = [1, -1, 0, 0] ## 동, 서, 남, 북 (좌우 움직임)
    
    queue = deque([(0,0,1)]) ## x좌표, y좌표, 현재까지 움직인 칸
    maps[0][0] = 2 ## 방문처리
    
    while queue:
        x, y, dis = queue.popleft()
        
        # print("***")
        # print(x, y, dis)
        # for line in maps:
        #     print(line)
        
        if x ==n and y == m :
            answer = dis
            break
        
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]
            if new_x >= 0 and new_x <= n and new_y >=0 and new_y <= m:
                if maps[new_x][new_y] == 1:
                    queue.append((new_x, new_y, dis+1))
                    maps[new_x][new_y] = 2 ## 방문처리
        
    if x != n or y != m: ## 최종 맵에 도달하지 못한 경우 
        answer = -1
    
    return answer

if __name__ == '__main__':
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))