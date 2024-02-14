## N개의 자연수 중에서 M개를 고른 수열
## 수열은 비내림차순이다. 
## (N개의 자연수는 중복이 있을 수 있다.) 
## 중복되는 수열을 여러번 출력하면 안 된다. 

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq = sorted(seq) ## 수열은 사전 순으로 증가하는 순서로 출력해야 한다. 
visited = [False] * n ## not in method보다 빠르게 구현할 수 있다. 

def dfs(sub, visited):
    
    if len(sub) == m:
        result = [seq[i] for i in sub]
        print(*result)
        return
    
    overlap = 0 ## depth 별로 중복을 막을 수 있는 방법 
    for i in range(len(seq)):
        if not visited[i] and seq[i] != overlap : 
            if sub and seq[sub[-1]] <= seq[i]:
                sub.append(i)
                visited[i] = True
                overlap = seq[i]
                dfs(sub, visited)
                sub.pop()
                visited[i] = False
            elif not sub:
                sub.append(i)
                visited[i] = True
                overlap = seq[i]
                dfs(sub, visited)
                sub.pop()
                visited[i] = False


dfs([], visited)