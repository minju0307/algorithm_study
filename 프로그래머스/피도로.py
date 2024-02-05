

def dfs(dungeons, idx, visited, k, d_list):
    print(idx)
    
    d_list.append(idx)
    k = k - dungeons[idx][1]
    
    print(d_list)
    print(visited)
    print(k)
    
    if k < min_p:
        ans.append(d_list)
        return ans
    
    ## 갈 수 있는 던전을 찾아서 방문
    for idx, d in enumerate(dungeons):
        if not visited[idx]:
            if dungeons[idx][0] <= k:
                visited[idx] = True
                result = dfs(dungeons, idx, visited, k, d_list)
                if result:
                    return result
                ## 백트래킹
                visited[idx] = False
                k = k + dungeons[idx][1]
                
    d_list.pop()
    return None
    
        


def solution(k, dungeons):
    original_k = k
    visited = [False for _ in range(len(dungeons))] ## 던전 방문 여부 표시
    d_list = [] ## 한번 방문할 때마다의 던전 리스트 
    global ans
    global min_p 
    ans = [] ## 전체 방문 코스 담아놓기 
    tmp = []
    for idx, d in enumerate(dungeons):
        tmp.append(d[0])
    min_p = min(tmp)
    print("min_p: ", min_p)
    
    for idx, d in enumerate(dungeons):
        visited[idx] = True
        dfs(dungeons, idx, visited, k, d_list)
        ## 백트래킹
        visited[idx] = False
        d_list = []
        k = original_k
        print("ans:", ans)
        print()
        
    answer = -1
    for a in ans:
        answer = max(answer, len(a))
        
    return answer

if __name__=='__main__':
    print(solution(80, [[80,20],[50,40],[30,10]]))