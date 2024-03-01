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

def dfs(start, sub, visited):
    
    if len(sub) == m:
        result = [seq[i] for i in sub]
        print(*result)
        return
    
    overlap = 0 ## depth 별로 중복을 막을 수 있는 방법 
    for i in range(start, n): ## 포인트 : 비내림차순이 되기 위하여 start 변수부터 탐색 (이전 뎁스 i보다 하나 큰 값)
        if not visited[i] and seq[i] != overlap : 
            sub.append(i)
            visited[i] = True
            overlap = seq[i]
            dfs(i+1, sub, visited) ## i+1를 start로 설정해서 현재보다 같거나 큰 숫자들만 탐색할 수 있도록 
            sub.pop()
            visited[i] = False


dfs(0, [], visited)