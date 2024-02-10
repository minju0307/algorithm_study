import sys 
input = sys.stdin.readline

n, m = map(int, input().strip().split())
teok = list(map(int, input().strip().split()))

## 이분 탐색의 범위
left = 0
right = max(teok)
answer = 0

while left <= right:
    
    mid = (left+right) // 2
    
    ## 손님이 가져갈 cut 된 양을 확인하기 
    cut = 0
    for i in teok:
        if i > mid:
            cut += (i-mid)
    
    ## 현재 손님이 가져간 cut이 m 보다 너무 크면 (현재가 정답(최적)일 수도 있음) -> mid의 오른쪽 부분 탐색하기 
    if cut >= m :
        left = mid +1
        answer = max(mid, answer) ## max 함수를 빼도 동일함
    
    ## 현재 손님이 가져간 cut이 m 보다 작은 경우 (아예 정답이 될 수 없음) -> mid의 왼쪽 부분 탐색하기 
    else:
        right = mid - 1

print(answer)
