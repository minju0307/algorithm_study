## N개의 자연수 중에서 M개를 고른 수열
## (N개의 자연수는 중복이 있을 수 있다.) 
## 중복되는 수열을 여러번 출력하면 안 된다. 

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq = sorted(seq) ## 수열은 사전 순으로 증가하는 순서로 출력해야 한다. 
visited = [False] * n
ans = []

def dfs(sub, visited):
    
    if len(sub) == m:
        result = [seq[i] for i in sub]
        ans.append(result) ## 여기서 not in 으로 확인하면 시간초과
        return 
    
    for i in range(len(seq)):
        if not visited[i]:
            visited[i] = True
            sub.append(i)
            dfs(sub, visited)
            sub.pop()
            visited[i] = False
            
            
dfs([], visited)
answers = sorted(list(set(map(tuple, ans)))) ## 모든 경우의 수에 대해서 마지막에 처리해주는 것이 필요 
for answer in answers:
    print(*answer)
