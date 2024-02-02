def solution(people, limit):
    people = sorted(people) 
    ships = [[0,0] for _ in range(len(people))] ## [현재 중량, 탄 사람의 숫자]
    count = 0
    
    for idx, p in enumerate(people):
        if idx == 0 : 
            ships[idx] = [p, 1]
            count +=1
            continue
        ## 이전 보트에 함께 타는 경우 
        if (ships[idx-1][0] + p <= limit) and (ships[idx-1][1] == 1):
            ships[idx-1][0] += p 
            ships[idx-1][1] += 1
            continue
        ## 새로운 보트에 타는 경우 
        else:
            ships[idx] = [p, 1]
            count += 1

    return count 

if __name__=='__main__':
    print(solution([70, 50, 80, 50], 100))