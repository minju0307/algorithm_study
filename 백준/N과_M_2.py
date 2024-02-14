## 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 
## 고른 수열은 오름차순이어야 한다. 

import sys
input = sys.stdin.readline

n, m = map(int, input().split()) 

def dfs(sub):
    ## 종료 조건
    if sub and len(sub) == m:
        print(*sub)
        return
    
    ## 순회
    for i in range(1, n+1):
        if not sub or (i not in sub and sub[-1] < i):
            sub.append(i)
            dfs(sub)
            sub.pop()


dfs([])