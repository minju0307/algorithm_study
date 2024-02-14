## N개의 자연수 중에서 M개를 고른 수열
## 같은 수를 여러 번 골라도 된다. 
## (N개의 자연수는 중복이 있을 수 있다.) 
## 중복되는 수열을 여러번 출력하면 안 된다. 

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq = sorted(seq) ## 수열은 사전 순으로 증가하는 순서로 출력해야 한다. 


def dfs (sub):
    
    if len(sub) == m :
        result = [seq[i] for i in sub]
        print(*result)
        return 
    
    overlap = 0 ## 같은 depth에서의 중복을 방지하기 위함
    for i in range(n):
        if seq[i] != overlap: ## visited를 확인하지 않아도 됨, 모든 숫자를 다 고려하여 뽑을 수 있음 
            sub.append(i)
            overlap = seq[i]
            dfs(sub)
            sub.pop()

dfs([])