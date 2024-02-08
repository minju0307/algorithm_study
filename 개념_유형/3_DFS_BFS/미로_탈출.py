from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

queue = deque([(0, 0, 1)]) ## (x좌표, y좌표, 최단 경로)

while queue:
    x, y, count = queue.popleft()
    if x == n-1 and y == m-1 :
        print(count)
        break
    if x < n-1 and graph[x+1][y] == 1: ## 아래로 갈 수 있다면
        queue.append((x+1, y, count+1))
    if y < m-1 and graph[x][y+1] == 1: ## 오른쪽으로 갈 수 있다면
        queue.append((x, y+1, count+1))