def solution(people, limit):
    people = sorted(people, reverse=True) 
    ships = [0]*len(people) ## 사람 수 만큼 배를 준비해놓기 
    
    for p in people:
        for idx, ship in enumerate(ships): 
            if ship + p <= limit: ## 기존 배에 태울 수 있으면 태우기 
                ships[idx] += p
                break
            else:
                continue ## 다른 배에 태우기, 모두 태울 수 없으면 새로운 배에 타기 

    return len(people) - ships.count(0)