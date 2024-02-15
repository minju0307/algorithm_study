import heapq

def dijkstra(start, distance, graph):
	q = []

	heapq.heappush(q, (0, start)) 
	distance[start]= 0

	while q:
		dist, now = heapq.heappop(q)
		
		if distance[now] < dist: ## 이미 방문했던 것 
			continue 
		
		## 해당 노드를 거쳐서 다른 노드로 가는 비용들을 확인하기 
		## 따라서 현재 노드와 연결된 다른 인접한 노드들을 확인
		for i in graph[now]:
			cost = dist + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost ## 현재 노드를 거치는 게 더 빠른 경우 최단 경로 갱신
				heapq.heappush(q, (cost, i[0])) ## 갱신된 경우에만 큐에 삽입 
        
        
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    distance = [int(1e9)] * (n+1)
    distance[0] = 0 ## 0번 인덱스는 사용하지 않음 
    
    ## 양방향 그래프, 모든 간선의 비용은 1
    for a,b in edge:
        graph[a].append((b ,1)) ## (노드, 비용) 
        graph[b].append((a, 1))
            
    dijkstra(1, distance, graph) ## 1번 노드에서 가장 멀리 떨어진 노드의 갯수 구하기
    
    return distance.count(max(distance))

if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))