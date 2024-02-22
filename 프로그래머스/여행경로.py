
## 주어진 항공권은 모두 사용해야 합니다.
## 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
## 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

## 그럼 전체 방문이 가능한 경로들을 모두 저장한 다음, 마지막에 정렬을 하는 것이 필요 
## 모든 티켓을 소진하였는지는 path에 추가한다음에 그 path들이 전체 티켓 개수 + 1 이 되는지 확인하면 됨 (종료 조건)

ans = []

def dfs(start, graph, visited, path, length):
    # print(path)
    global ans
    if len(path) == length:
        ans.append(path)
        print(ans)
        return
    
    for idx, next in enumerate(graph[start]):
        if not visited[start][idx]:
            visited[start][idx] = True
            path.append(next)
            dfs(next, graph, visited, path, length)
            path.pop()
            visited[start][idx] = False
    return

def solution(tickets):
    global ans
    
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

    print()
    print(ans)
    
    # answer = sorted(ans)[0]
    
    return ans

if __name__ == '__main__':
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))