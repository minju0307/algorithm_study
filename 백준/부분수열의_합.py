import sys
input = sys.stdin.readline

n, s = map(int, input().split())
array = list(map(int, input().split()))
visited = [False] * n
answer = 0

def dfs(sub, visited):
    global answer
    
    if sub :
        hap = sum([array[i] for i in sub])
        # print("***")
        # print(sub)
        # print([array[i] for i in sub])
        # print()
        if hap == s: 
            # print(" >>> 위에 정답!")
            # print()
            answer += 1
    
    for i in range(len(array)):
        if sub[-1] < i :
            sub.append(i)
            visited[i] = True
            dfs(sub, visited)
            visited[i] = False
            sub.pop()


for i in range(len(array)):
    visited[i] = True
    dfs([i], visited)
    visited[i] = False
    
print(answer)  
