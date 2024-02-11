
def solution(word):
    global count
    vowels = 'AEIOU'
    
    count = 1
    level = 1
    previous = 'A'
    stack = [previous]
    
    while stack:
        now = stack.pop()
        count += 1
        if level == 5:
            level = 1
        
        if previous[-1] == 'U':
            level += 1
            current = previous[:-level] + now
        elif level > 1:
            current = previous + now
        else:
            current = previous[:-1] + now
        
        print(current)
        print(level)
        
            
        if current == word:
            break
        
        if len(current) < 5:
            stack.extend(list(vowels)[::-1])
        
        # print(stack)
        previous = current
    
    
    return count

if __name__=="__main__":
    print(solution("AAE"))