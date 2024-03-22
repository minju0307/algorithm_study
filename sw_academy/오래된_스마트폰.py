from collections import deque

T = int(input())
operation_dict = {"1":"+", "2":"-", "3":"*", "4":"/"}

## 숫자 터치만으로 만들 수 있는 3자리 이하의 수 만들기
def make_num(depth, now, can_num):
    if depth == 3:
        return 
    
    for num in can_num:
        next_num = now*10+num
        if next_num <= 999:
            nums.append(next_num)
            if dp[next_num] <= depth + 1: ## 0이 앞에 와서 똑같은 숫자에 대한 recursion이 일어나는 것을 방지하기 위하여
                continue
            dp[next_num] = depth + 1
            make_num(depth+1, next_num, can_num)
            

## 계산하는 함수 (조건들을 반영하기)
def calculation(n1, n2, operator):
    if operator == "+":
        result = n1+n2
    elif operator == "-":
        result = n1-n2
    elif operator == "*":
        result = n1*n2
    else:
        if n2 == 0:
            return False
        else:
            result = n1//n2
    if result < 0 or result > 999:
        return False
    else:
        return result


for test_case in range(1, T+1):
    # 입력 받기 
    n, o, m = map(int, input().split())
    can_num = list(map(int, input().split()))
    can_op = input().split()
    target = int(input().rstrip())
    
    nums = can_num[:]
    dp = [21 for _ in range(1000)] ## 계산 횟수를 기록하는 dp 테이블 
    for now in can_num:
        dp[now] = 1
        make_num(1, now, can_num) ## 운영할 수 있는 세자리 수를 모두 만들어놓기 
    nums = sorted(list(set(nums)))
    
    ## 만약 숫자만으로 만들 수 있으면 프린트
    if dp[target] < 21:
        print(f"#{test_case}", dp[target])
        continue
    
    ## 그것이 아니라면 BFS로 순회하기 
    q = deque(nums)

    while q:
        now = q.popleft()
        
        ## 순회하기 
        for num in nums:
            for op in can_op:
                result = calculation(now, num, operation_dict[op])
                if result and dp[result] > dp[now] + dp[num] + 1 : ## 문제 조건을 벗어나지 않는 숫자가 나왔다면 
                    dp[result] = dp[now] + dp[num] + 1 ## operator와 = 
                    q.append(result)
    
    if dp[target] == 21:
        print(f"#{test_case}", -1)
        continue
    else:
        print(f"#{test_case}", dp[target]+1)
        continue


    
'''
1
5 3 10
8 7 1 2 6
2 4 3
981
'''

'''
5
6 4 5
0 1 2 3 4 7
1 2 3 4
5
3 1 4
1 6 5
1
0
7 3 6 
1 8 0 2 6 7 9
2 1 4
91
5 2 10
4 0 5 3 9
3 4
28
5 3 10
8 7 1 2 6
2 4 3
981
'''