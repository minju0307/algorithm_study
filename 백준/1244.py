import sys
input = sys.stdin.readline

s_num = int(input().rstrip())
switch = list(range(1, s_num+1))
status = list(map(int, input().rstrip().split()))

n = int(input().rstrip())
for _ in range(n):
    sex, num = map(int, input().split())
    
    if sex == 1: ## 남학생인 경우
        for i in switch:
            if i % num == 0:
                status[i-1] = 1-status[i-1]
    else : ## 여학생인 경우 
        ## num을 기준으로 최대 대칭이 되는 구간을 찾기 
        ## 대칭되는 구간들의 스위치 상태를 모두 바꾸기 
        status[num-1] = 1- status[num-1]
        for i in range(1, s_num//2):
            if 0<= num-1-i and num-1+i < s_num and status[num-1-i] == status[num-1+i]:
                status[num-1-i] = 1 - status[num-1-i]
                status[num-1+i] = 1 - status[num-1+i]
            else:
                break

for idx, s in enumerate(status):
    if (idx+1)%20 == 0 :
        print(s)
    else:
        print(s, end=" ")