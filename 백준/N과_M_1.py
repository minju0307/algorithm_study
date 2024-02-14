## 1부터 n까지의 자연수 중에서 중복없이 m개를 고른 수열

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
        if i not in sub:
            sub.append(i)
            dfs(sub)
            sub.pop()

dfs([])