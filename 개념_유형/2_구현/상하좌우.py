## 이 문제에서는 연산 횟수가 이동 횟수에 비례하기 때문에, 시간 복잡도가 O(N)으로 넉넉한 편이다. 


import sys
input = sys.stdin.readline

n = int(input().strip())
move = list(input().split())

map = [ [i for i  in range(n)] for _ in range(n)] ## 맵 초기화 
dx = [1, -1, 0, 0] ## R L D U
dy = [0, 0, 1, -1] ## R L D U

x, y = 0, 0 ## 현재 위치 
for m in move:
    if m == 'R':
        x += dx[0]
        y += dy[0]
        if (x < 0 or x >= n) or (y < 0 or y >= n): ## 공간 밖은 무시 
            x -= dx[0]
            y -= dy[0]
    elif m == 'L':
        x += dx[1]
        y += dy[1]
        if (x < 0 or x >= n) or (y < 0 or y >= n): ## 공간 밖은 무시 
            x -= dx[1]
            y -= dy[1]
    elif m == 'D':
        x += dx[2]
        y += dy[2]
        if (x < 0 or x >= n) or (y < 0 or y >= n): ## 공간 밖은 무시 
            x -= dx[2]
            y -= dy[2]
    else:
        x += dx[3]
        y += dy[3]
        if (x < 0 or x >= n) or (y < 0 or y >= n): ## 공간 밖은 무시 
            x -= dx[3]
            y -= dy[3]
    # print(x, y)
    
print(x+1, y+1) ## 최종 출력 
    

