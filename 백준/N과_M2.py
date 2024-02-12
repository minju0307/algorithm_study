import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False]*(n+1) ## 중복을 피하는 효과

def dfs(sequence, visited):
    if len(sequence) == m:
        print(*sequence)
        return 
    
    for i in range(1, n+1):
        if not visited[i] and sequence[-1] < i :
            sequence.append(i)
            visited[i] = True
            dfs(sequence, visited)
            visited[i] = False
            sequence.pop()
            

for i in range(1, n+1):
    visited[i] = True
    dfs([i], visited)
    visited[i] = False