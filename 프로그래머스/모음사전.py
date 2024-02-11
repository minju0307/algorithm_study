count = 0
answer = 0

def dfs(now, word, vowels):
    ## 방문하자마자 해야 하는 일
    global count
    global answer
    count +=1 
    
    ## 종료 조건
    if now == word :
        answer = count
        return
    
    ## 순회
    if len(now) < 5:
        for v in vowels:
            dfs(now+v, word, vowels)
    
def solution(word):
    global count
    global answer
    
    vowels = 'AEIOU'
    for v in vowels:
        dfs(v, word, vowels)
    return answer

if __name__=="__main__":
    print(solution("EIO"))