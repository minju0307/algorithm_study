from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

# for ll in graph:
#     print(ll)
# print()

count = 0
queue = deque([])

for i, line in enumerate(graph):
    for j, type in enumerate(line):
        # print(">>>")
        # print(i, j)
        if graph[i][j] == 0:
            count += 1
            queue.append((i, j))
            
            while queue:
                x, y = queue.popleft()
                # print("***")
                # print(x, y)
                graph[x][y] = 2 ## 방문처리 
                if x > 0 and graph[x-1][y]==0: ##위로 갈 수 있으면 
                    queue.append((x-1, y))
                if x < n-1 and graph[x+1][y]==0: ## 아래로 갈 수 있으면 
                    queue.append((x+1, y))
                if y > 0 and graph[x][y-1]==0: ## 왼쪽으로 갈 수 있으면 
                    queue.append((x, y-1))
                if y < m-1 and graph[x][y+1]==0: ## 오른쪽으로 갈 수 있으면
                    queue.append((x, y+1))
                # print(queue)
                # for ll in graph:
                #     print(ll)
                # print(count)
                # print()
                    
print(count)
