answer = 0

def dfs(i, numbers, hap, visited, target):
    global answer 
    if i == len(numbers):
        # print(f"   >>> depth: {i}, hap : {hap}")
        if hap == target:
            answer += 1
            return
        else:
            return 
    
    if not visited[i]:
        # print("***")
        # print(f"depth : {i}, n : {numbers[i]}")
        visited[i] = True
        dfs(i+1, numbers, hap+numbers[i], visited, target)
        dfs(i+1, numbers, hap-numbers[i], visited, target) 
        visited[i] = False

def solution(numbers, target):
    global answer
    visited = [False] * len(numbers)
    dfs(0, numbers, 0, visited, target)
    
    return answer

if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))