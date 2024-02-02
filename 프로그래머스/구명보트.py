from collections import deque

def solution(people, limit):
    people = sorted(people, reverse=True)
    queue = deque(people)
    count = 0
    
    while queue:
        if len(queue)>1 and queue[0] + queue[-1] <= limit: ## 둘을 한 보트에 타게 만든다. 
            queue.popleft()
            queue.pop()
            count += 1
        else:
            queue.popleft() ## 무거운 한 사람만 보트에 타게 만든다. 
            count += 1
    
    
    return count 