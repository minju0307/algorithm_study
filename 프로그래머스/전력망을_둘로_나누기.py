def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union (parent, i, j):
    ir = find_parent(parent, i)
    jr = find_parent(parent, j)
    if ir < jr:
        parent[jr] = ir
    else:
        parent[ir] = jr
    

def solution(n, wires):
    answer = n
    
    for remove in wires:
        parent = [i for i in range(n+1)] ## parent 행렬을 자기 자신으로 초기화
        
        for wire in wires: ## 각 edge에 대해서,
            if wire == remove: ## 현재 wire가 삭제된 것이면 continue
                continue
            union(parent, wire[0], wire[1]) ## edge가 이어져 있을 때는 union 

        ## 부모 리스트 root 값으로 돌려놓기 
        for i in range(1, n+1):
            parent[i] = find_parent(parent, i)
        parent.remove(0)
        keys = list(set(parent)) ## 두 개로 나뉘기 때문에
        answer = min(abs(parent.count(keys[0])-parent.count(keys[1])), answer)


    return answer

if __name__=="__main__":
    print(solution(4, [[1,2],[2,3],[3,4]]))