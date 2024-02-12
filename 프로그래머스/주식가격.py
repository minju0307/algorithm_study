from collections import deque

def solution(prices):
    times = []
    queue = deque(prices)
    
    while queue:
        # print("***")
        # print(queue)
        time = 0
        price = queue.popleft()
        
        for now in queue:
            time += 1
            if price > now:
                break
            
        times.append(time)
        
    return times               

"""
def solution(prices):
    times = []
    
    for idx in range(len(prices)):
        time = 0
        
        price = prices[idx]
        for now in prices[idx+1:]:
            time += 1
            if price > now:
                break
            
        times.append(time)
        
    return times 
"""

if __name__=='__main__':
    print(solution([1, 2, 3, 2, 3])) ## return 4,3,1,1,0