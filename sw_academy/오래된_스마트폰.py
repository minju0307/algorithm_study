from collections import deque

T = int(input())
operation_dict = {"1":"+", "2":"-", "3":"*", "4":"/"}

answers = []

def calculation(_list):
    nums = []
    ops = []
    num = ''
    for x in _list:
        if type(x) == int:
            num += str(x)
        else:
            nums.append(int(num))
            ops.append(x)
            num = ''
    nums.append(int(num))
    
    stack1 = nums[::-1]
    stack2 = ops[::-1]
    
    while stack2:
        n1 = stack1.pop()
        n2 = stack1.pop()
        x = stack2.pop()
        
        if x == "+":
            stack1.append(n1+n2)
        elif x == "-":
            stack1.append(n1-n2)
        elif x == "*":
            stack1.append(n1*n2)
        else:
            if n2 == 0:
                return False
            else:
                stack1.append(n1//n2)
    
    return stack1[0]


for test_case in range(1, T+1):
    tmp_answers = []
    # 입력 받기 
    n, o, m = map(int, input().split())
    can_num = list(map(int, input().split()))
    can_op = input().split()
    target = int(input().rstrip())
    
    q = []
    for num in can_num:
        q.append((1, num, [num])) ## 버튼 누른 횟수, 계산 결과, 계산 과정
    q = deque(q)
    # print(q)
    
    ## BFS로 가능한 경우를 모두 찾기 
    while q:
        # print("***")
        # print(q)
        
        count, result, history = q.popleft()
        # print(">>>")
        # print(count, result, history)
        
        ## 종료 조건 
        if result == target:
            if ("+" in history) or ("-" in history) or ("*" in history) or ("/" in history):
                answer = count + 1
                break
            else:
                answer = count
                break
        elif count >= m :
            answer = -1
            break
        
        ## 숫자에 해당하는 것들을 다음 queue에 넣기 (숫자가 3개 이상 연달아 갈 수 없음)
        for num in can_num:
            next_result = calculation(history+[num])
            if next_result and 0 <= next_result <= 999:
                q.append((count+1, next_result, history+[num]))
        
        ## 만약 현재가 숫자라면, 연산자에 해당하는 것들을 다음 queue에 넣기
        if type(history[-1]) == int:
            for op in can_op:
                q.append((count+1, result, history+[operation_dict[op]]))
                        
    print(f"#{test_case}", answer)

# for idx, answer in enumerate(answers):
#     print(f"#{idx+1}", answer)

    
'''
1
6 4 5
0 1 2 3 4 7
1 2 3 4
5
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