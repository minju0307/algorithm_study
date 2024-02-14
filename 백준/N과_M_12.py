## N개의 자연수 중에서 M개를 고른 수열
## (N개의 자연수는 중복이 있을 수 있다.)
## 같은 수를 여러 번 골라도 된다. 
## 수열은 비내림차순 수열이어야 한다. 
## 중복되는 수열을 여러번 출력하면 안 된다. 

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq = sorted(seq) ## 수열은 사전 순으로 증가하는 순서로 출력해야 한다. 

def dfs(sub):
    
    if len(sub) == m :
        result = [seq[i] for i in sub]
        print(*result)
        return
    
    overlap = 0
    for i in range(n):
        if seq[i] != overlap :
            if not sub:
                sub.append(i)
                overlap = seq[i]
                dfs(sub)
                sub.pop()
            elif seq[sub[-1]] <= seq[i]:
                sub.append(i)
                overlap = seq[i]
                dfs(sub)
                sub.pop()
                

dfs([])