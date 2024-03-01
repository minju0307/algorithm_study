## N개의 자연수 중에서 M개를 고른 수열
## (N개의 자연수는 중복이 있을 수 있다.) 
## 중복되는 수열을 여러번 출력하면 안 된다. 

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq = sorted(seq) ## 수열은 사전 순으로 증가하는 순서로 출력해야 한다. 
visited = [False] * n

def dfs(sub, visited):
    
    if len(sub) == m:
        result = [seq[i] for i in sub]
        print(*result)
        return 
    
    ## 각 뎁스별로 overlap이 일어나는지 아닌지를 확인하는 변수를 정의 
    overlap = 0  ## (각 뎁스별로 같은 숫자는 확인하지 않게 됨, 정렬이 되어 있기 때문에 사용 가능)
    for i in range(len(seq)):
        if not visited[i] and overlap != seq[i]:
            visited[i] = True
            sub.append(i)
            overlap = seq[i]
            dfs(sub, visited)
            sub.pop()
            visited[i] = False
            
            
dfs([], visited)
