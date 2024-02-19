answer = 0

def dfs(i, numbers, hap, target):
    global answer 
    if i == len(numbers):
        if hap == target:
            answer += 1
            return
        else:
            return 
    dfs(i+1, numbers, hap+numbers[i], target)
    dfs(i+1, numbers, hap-numbers[i], target) 


def solution(numbers, target):
    global answer
    dfs(0, numbers, 0, target)
    
    return answer

if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))