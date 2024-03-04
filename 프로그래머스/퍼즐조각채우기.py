from collections import deque

def find (board, f):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    blocks = []
    visited = [[0]*len(board) for _ in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board)):
            block = []
            if board[i][j] == f and visited[i][j]==0:
                visited[i][j] = 1
                block.append((i, j))
                queue = deque(block)
                
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny =  y + dy[k]
                        
                        if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == f and visited[nx][ny]==0:
                            visited[nx][ny] = 1
                            block.append((nx, ny))
                            queue.append((nx, ny))
                
                blocks.append(block)
    
    return blocks

def shape(block):
    xs = []
    ys = []
    for x, y in block:
        xs.append(x)
        ys.append(y)
        
    height = max(xs) - min(xs) + 1
    width = max(ys) - min(ys) + 1
    
    table = [[0]*width for _ in range(height)]
    
    for x, y in block:
        table[x-min(xs)][y-min(ys)] = 1
    
    return table

def rotate(array_2d):
    n = len(array_2d) ## 행의 길이 
    m = len(array_2d[0]) ## 열의 길이 
    table = [[0]*n for _ in range(m)] ## 회전한 결과를 표시하는 배열 
    
    for i in range(n):
        for j in range(m):
            table[j][n-i-1] = array_2d[i][j]
    
    return table

def solution(game_board, table):
    
    answer = 0
    
    empty = find(game_board, 0)
    puzzles = find(table, 1)
    
    for emp in empty:
        flag = False
        table = shape(emp) ## 현재 비어있는 공간 
        
        for puzzle in puzzles: ## 모든 퍼즐들을 현재 비어있는 공간에 대입하기 
            if flag == True:
                break
            
            puzzle_shape = shape(puzzle)
            for _ in range(4):
                puzzle_shape  = rotate(puzzle_shape)
                if table == puzzle_shape: ## 비는 칸이 없이 꼭 맞춰져야 한다.
                    for line in puzzle_shape:
                        answer += line.count(1)
                    flag = True
                    puzzles.remove(puzzle) ## 다음에 중복으로 카운트되지 않게 하기 위해서
                    break
                
    return answer

if __name__ == '__main__':
    print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))