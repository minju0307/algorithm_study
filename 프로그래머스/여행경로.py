ans = []

def dfs(start, graph, visited, path, length):
    
    # print(path)
    if len(path) == length:
        ans.append(path[:]) ## 복사하여 넣는 것의 유의할 필요 
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

    dfs("ICN", graph, visited, ["ICN"], len(tickets)+1)
    
    return min(ans)

if __name__ == '__main__':
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))