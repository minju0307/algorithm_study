import sys
input = sys.stdin.readline

n = int(input().rstrip())
maps = []
for _ in range(n):
    maps.append(list(input().rstrip()))
visited = [[False]*n for _ in range(n)]
    
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(i, j, maps, visited):
    visited[i][j] = True
    pos_i.append(i)
    pos_j.append(j)
    
    for k in range(4):
        ni = i+dx[k]
        nj = j+dy[k]
        
        if 0<=ni<n and 0<=nj<n and not visited[ni][nj] and maps[ni][nj]=='*':
            dfs(ni, nj, maps, visited)

type = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == "*" and not visited[i][j]:
            pos_i=[]
            pos_j=[]
            dfs(i, j, maps, visited)
            # print(pos_i)
            # print(pos_j)
            
            if type == 0:
                print(pos_i[1]+1, pos_j[1]+1) ## 심장의 위치 
                left = 0 
                right = 0 
                center = 0 
                for k in pos_j[2:]:
                    if k < pos_j[1]:
                        left += 1
                    elif k > pos_j[1]:
                        right += 1
                    else:
                        center += 1
                answers = [left, right, center]
            else:
                answers.append(len(pos_j))
                
            type += 1

print(*answers)