## N개의 자연수 중에서 M개를 고른 수열
## (N개의 자연수는 중복이 있을 수 있다.) 
## 중복되는 수열을 여러번 출력하면 안 된다. 

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq = sorted(seq) ## 수열은 사전 순으로 증가하는 순서로 출력해야 한다. 
ans = []

def dfs(sub):
    
    if len(sub) == m:
        result = [seq[i] for i in sub]
        if result not in ans: ## 중복되는 수열을 출력하면 안 된다.
            print(*result)
            ans.append(result)
        return 
    
    for i in range(n): ## 수열의 인덱스에 대하여 
        if i not in sub:
            sub.append(i)
            dfs(sub)
            sub.pop()
            

dfs([])