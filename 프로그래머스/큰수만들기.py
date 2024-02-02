
def solution(number, k):
    number = list(number)
    
    window = len(number)-k
    start = 0
    
    while len(number) > window:
        # print("***")
        # print(start)
        number.remove(min(number[start:window]))
        # print(number)
        # print()
        start+=1
        
    return ''.join(number)

if __name__=='__main__':
    print(solution("4177252841", 4))