def solution(m, n, puddles):
    
    maps = [[0]*m for _ in range(n)]
    for _m, _n in puddles:
        maps[_n-1][_m-1] = -1    
        
    maps[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i > 0 and maps[i][j] != -1 and maps[i-1][j] != -1:
                maps[i][j] += maps[i-1][j]
            if j > 0 and maps[i][j] != -1 and maps[i][j-1] != -1:
                maps[i][j] += maps[i][j-1]

    answer = maps[n-1][m-1]
    return answer % 1000000007

if __name__ == '__main__':
    print(solution(4, 3, [[2, 2]]))