## N개의 자연수 중에서 M개를 고른 수열
## 같은 수를 여러 번 골라도 된다.
## 고른 수열은 비내림차순이어야 한다. 

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq = sorted(seq) ## 수열은 사전 순으로 증가하는 순서로 출력해야 한다. 

def dfs(sub):
    if len(sub) == m:
        print(*sub)
        return
    
    for i in seq:
        if not sub or sub[-1] <= i:
            sub.append(i)
            dfs(sub)
            sub.pop()
            
dfs([])