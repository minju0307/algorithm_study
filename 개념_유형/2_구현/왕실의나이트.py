import sys 
input = sys.stdin.readline

column = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
pos = input().strip()

x = column[pos[0]] ## 좌우 움직임
y = int(pos[1]) ## 상하 움직임 

## 움직임 정의 (총 8가지)
dx = [2, 2, -2, -2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, 2, 2, -2, -2]

count = 0
for i in range(8):
    x_move = x + dx[i]
    y_move = y + dy[i]
    if x_move > 0 and x_move <= 8 and y_move > 0 and y_move <= 8:
        count +=1

print(count)
