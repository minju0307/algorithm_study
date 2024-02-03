
def solution(number, k):
    stack = []
    
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k-=1
        stack.append(num) 
        
    if len(stack) > len(number)-k: ## 모두 다 같은 숫자로 이루어져 있는 경우 
        stack = stack[:len(number)-k]
    
    return ''.join(stack)

if __name__=='__main__':
    print(solution("4177252841", 4))