def solution(n, results):
    answer = 0
    graph = [[0]*(n) for _ in range(n)]
    
    for a,b in results:
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = -1
    
    # for line in graph:
    #     print(line)
    # print()
    
    for k in range(n):
        for a in range(n):
            for b in range(n):
                
                if a == b or graph[a][b] in [1,-1]: ## 자기 자신이거나, 이미 둘의 승패를 알고 있다면 넘어가기 
                    continue
                
                if graph[a][k] == graph[k][b] == 1: ## a가 k를 이기고, k가 b를 이긴 것이 있으면
                    graph[a][b] = 1 ## a가 b를 이긴 것
                    graph[b][a] = -1 ## b가 a에게 진 것 
                    graph[k][a] = -1 ## k는 a에게 진 것 
                    graph[b][k] = -1 ## b는 k에게 진 것 
    
    # for line in graph:
    #     print(line)
    
    for line in graph:
        if line.count(0) == 1: ## 자기 자신 빼고 모든 결과를 알고 있으면 순위를 알 수 있음 
            answer += 1
    
    return answer

if __name__ == '__main__':
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))