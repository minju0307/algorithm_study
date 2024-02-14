## N개의 자연수 중에서 M개를 고른 수열
## N개는 모두 다른 수이다.

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
        if i not in sub:
            sub.append(i)
            dfs(sub)
            sub.pop()
    

dfs([])