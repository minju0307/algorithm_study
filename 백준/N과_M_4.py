## 1부터 N까지 자연수 중에서 M개를 고른 수열
## 같은 수를 여러 번 골라도 된다.
## 고른 수열은 비내림차순이어야 한다. 

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def dfs(sub):
    
    if len(sub) == m:
        print(*sub)
        return
    
    for i in range(1, n+1):
        if not sub or (sub[-1] <= i):
            sub.append(i)
            dfs(sub)
            sub.pop()

dfs([])