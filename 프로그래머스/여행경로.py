ans = []

def dfs(start, graph, visited, path, length):
    
    print("***")
    print(path)
    if len(path) == length:
        ans.append(path[:]) ## deepcopy 필요, shallow copy 인 경우 "ICN" 으로 path 가 변환될 수 있음   
        return 
    
    if start in graph.keys(): ## 런타임 에러 방지 
        for idx, next in enumerate(graph[start]):
            if not visited[start][idx]:
                visited[start][idx] = True
                path.append(next)
                dfs(next, graph, visited, path, length)
                path.pop()
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

    dfs("JFK", graph, visited, ["JFK"], len(tickets)+1)

    
    return min(ans)

if __name__ == '__main__':
    print(solution([["JFK", "KUL"],["JFK", "NRT"], ["NRT", "JFK"]]))