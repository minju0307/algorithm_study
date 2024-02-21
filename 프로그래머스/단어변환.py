from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    visited = [False] * len(words)
    queue = deque([(begin, 0)])
    
    while queue:
        current, dis = queue.popleft()
        
        if current == target:
            break
        
        for idx, w in enumerate(words):
            if not visited[idx]:
                correct = 0
                wrong = 0
                for new, cur in zip(list(w), list(current)):
                    if new == cur:
                        correct +=1
                    else:
                        wrong += 1
                if correct ==  len(current)-1:
                    queue.append((w, dis+1))
                    visited[idx] = True
                    
    return dis

if __name__ == '__main__':
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))