## 이 문제에서는 연산 횟수가 이동 횟수에 비례하기 때문에, 시간 복잡도가 O(N)으로 넉넉한 편이다. 


import sys
input = sys.stdin.readline

n = int(input().strip())
move = list(input().split())

map = [ [i for i  in range(n)] for _ in range(n)] ## 맵 초기화 
dx = [1, -1, 0, 0] ## R L D U
dy = [0, 0, 1, -1] ## R L D U
move_types = ['R', 'L', 'D', 'U']

x, y = 0, 0 ## 현재 위치 
for m in move:
    idx = move_types.index(m)
    x += dx[idx]
    y += dy[idx]
    if (x < 0 or x >= n) or (y < 0 or y >= n): ## 공간 밖은 무시 
        x -= dx[idx]
        y -= dy[idx]
        
    # print(x, y)
    
print(x+1, y+1) ## 최종 출력 
    

