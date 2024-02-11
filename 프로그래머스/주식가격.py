from collections import deque 

def solution(prices):
    times = [0] * len(prices)
    queue = deque([(0, 0)]) ## (주식 가격 idx, 가격이 떨어지지 않은 시간)
    
    while queue:
        
        if queue[-1][0] == len(prices):
            break
        
        print("***")
        print(queue)
        
        for _ in range(len(queue)):
            idx, time = queue.popleft()
            
            if idx < len(prices)-1 and prices[idx] <= prices[idx+1] :
                queue.append((idx, time+1))
                times[idx] = time
            elif idx < len(prices)-1 and prices[idx] > prices[idx+1] :
                times[idx] = time + 1
            else:
                times[idx] = time
        
        queue.append((idx+1, 0))
    
    return times


if __name__=='__main__':
    print(solution([1, 2, 3, 2, 3])) ## return 4,3,1,1,0