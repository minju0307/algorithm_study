ans = []

def dfs(start, tickets, visited, path, length):

    if len(path) == length:
        ans.append(path[:]) ## deepcopy 필요, shallow copy 인 경우 "ICN" 으로 path 가 변환될 수 있음   
        return 
    
    for idx, (a, b) in enumerate(tickets):
        if start == a and not visited[idx]:
            visited[idx] = True
            path.append(b)
            dfs(b, tickets, visited, path, length)
            path.pop()
            visited[idx] = False
    return

def solution(tickets):
    visited = [False]*len(tickets)
    dfs("ICN", tickets, visited, ["ICN"], len(tickets)+1)
    
    return min(ans)

if __name__ == '__main__':
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))