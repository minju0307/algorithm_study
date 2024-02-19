def dfs(i, computers, visited):
    visited[i] = True
    
    for j in range(len(computers)):
        if not visited[j] and computers[i][j] == 1:
            dfs(j, computers, visited)


def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(i, computers, visited)
            answer += 1
    
    return answer