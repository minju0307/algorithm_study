import sys
input = sys.stdin.readline

## 입력 받기 
n, m = map(int, input().split()) ## n이 상하, m이 좌우 
x, y, d = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))
    
directions = {0:3, 1:0, 2:1, 3:2} ## 반시계 방향 회전을 정의 
back_directions = {0:2, 2:0, 1:3, 3:1} ## 뒤로 한칸 가는 방향을 정의 
dx = [-1, 0, 1, 0] ## 북동남서 (x가 상하)
dy = [0, 1, 0, -1] ## 북동남서 (y가 좌우)

count = 1 ## 캐릭터가 방문한 칸 수 
while True:
    for i in range(4):
        ## 1단계 : 방향 회전 
        d = directions[d]
        
        ## 2단계 : 회전한 방향으로 이동 가능하면 이동, 아니면 continue (1단계로 이동)
        
        ## 맵을 벗어나지 않았을 때
        if x+dx[d] >= 0 and x+dx[d] < n and y+dy[d] >= 0 and y+dy[d] < m: 
            ## 바다도 아니고, 아직 방문하지 않았다면, 
            if maps[x+dx[d]][y+dy[d]] == 0 : 
                ## 방문처리
                maps[x+dx[d]][y+dy[d]] = 2 
                count += 1
                ## 해당 위치로 이동 
                x = x+dx[d] 
                y = y+dy[d]
                break
        else: 
            continue  
    
    ## 3단계 : 4방향 모두 갈 수 없는 경우  
    if i == 3:
        d = directions[d] ## 원래의 방향을 바라보기 
        ## 한 칸 뒤로 갈 수 있으면 원래 있던 곳으로 돌아가기 
        if x+dx[back_directions[d]] >= 0 and x+dx[back_directions[d]] < n and y+dy[back_directions[d]] >= 0 and y+dy[back_directions[d]] < m:
            if maps[x+dx[back_directions[d]]][y+dy[back_directions[d]]] == 0 or maps[x+dx[back_directions[d]]][y+dy[back_directions[d]]] == 2:
                x = x+dx[back_directions[d]]
                y = y+dy[back_directions[d]]
        ## 이동할 수 없는 경우에는 종료하기 
            else:
                break

print(count)
                
                
        
        
        
        
