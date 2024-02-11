from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    answer = 1 ## 다리를 건너는 데에 필요한 시간 
    queue = deque([(0, 1)]) ## (트럭 인덱스, 지나고 있는 다리 길이)
    
    while queue:
        answer += 1
        hap = 0
        
        for _ in range(len(queue)):
            print("***")
            print(queue)
        
            idx, length = queue.popleft()
            
            ## 다리를 아직 지나지 않았다면 다시 넣어주기 
            if length < bridge_length:
                queue.append((idx, length+1))
                hap += truck_weights[idx]
        
        ## 추가로 올릴 수 있는 트럭이 있다면 
        if idx < len(truck_weights)-1 and hap + truck_weights[idx+1] <= weight:
            queue.append((idx+1, 1))
        
    return answer

if __name__=='__main__':
    print(solution(2, 10, [7,4,5,6]))