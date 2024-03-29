from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    maps = [[-1]*102 for _ in range(102)] ## maps 의 최솟값을 어떻게 설정? 
    
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rec) ## 좌표를 두 배로 해주기 
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                ## 직사각형의 내면인 경우에는 무조건 0으로 채우기 
                if x1 < x < x2 and y1 < y < y2:
                    maps[x][y] = 0
                ## 다른 직사각형의 내부가 아니면서 현재 직사각형의 테두리 일 때 1로 채우기
                elif maps[x][y] != 0:
                    maps[x][y] = 1
    
    queue = deque([(characterX*2, characterY*2)]) ## (x좌표, y좌표)
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    visited = [[0]*102 for _ in range(102)]
    visited[characterX*2][characterY*2] = 1
     
     
    while queue:
        x, y = queue.popleft()
        
        if x == itemX*2 and y == itemY*2:
            answer = (visited[x][y]-1) // 2
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] +1
        
    return answer

if __name__ == '__main__':
    print(solution([[1, 1, 4, 4], [2, 2, 5, 5], [3, 3, 7, 8]], 1, 1, 5, 3))