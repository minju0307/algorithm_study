
def dfs(i, j, table, visited):
    
    if i < 0 or i >= len(table) or j < 0 or j >= len(table):
        return 
    
    if table[i][j] == 1 and visited[i][j] == 0:
        visited[i][j] = 1
        dfs(i-1, j, table, visited) 
        dfs(i+1, j, table, visited) 
        dfs(i, j-1, table, visited)
        dfs(i, j+1, table, visited) 
        return 
    
    return
        

def solution(game_board, table):
    
    puzzle_table = [[0]*len(table) for _ in range(len(table))]
    
    ## table로부터 퍼즐 조각 찾기 
    tmp = 0
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == 1 and puzzle_table[i][j] == 0:
                dfs(i, j, table, puzzle_table)
                tmp += 1
    print(tmp)
    for line in puzzle_table:
        print(line)
    
    ## game board 에서 빈칸 채우기 
    
    
    answer = -1
    return answer

if __name__ == '__main__':
    print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))