
## 주어진 항공권은 모두 사용해야 합니다.
## 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
## 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

## 그럼 전체 방문이 가능한 경로들을 모두 저장한 다음, 마지막에 정렬을 하는 것이 필요 
## 모든 티켓을 소진하였는지는 path에 추가한다음에 그 path들이 전체 티켓 개수 + 1 이 되는지 확인하면 됨 (종료 조건)

ans = []

def dfs(start, graph, visited, path, length):
    path.append(start)
    print(path)
    
    if len(path) == length:
        print(">>>")
        ans.append(path)
        return 
    
    for idx, next in enumerate(graph[start]):
        if not visited[start][idx]:
            visited[start][idx] = True
            dfs(next, graph, visited, path, length)
            visited[start][idx] = False
    return 

def solution(tickets):
    graph = dict()
    visited = dict()
    for a, b in tickets:
        if a not in graph.keys():
            graph[a] = [b]
            visited[a] = [False]
        else:
            graph[a].append(b)
            visited[a].append(False)
    
    print(graph)
    print()
    
    dfs("ICN", graph, visited, [], len(tickets)+1)
    
    answer = sorted(ans)[0]
    
    return answer

if __name__ == '__main__':
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))