import sys

input = sys.stdin.readline

n = int(input().rstrip())
answers = [] 

for _ in range(n):
    students = list(map(int, input().split()))
    
    count = 0
    current = []
    for i in students[1:]:
        current.append(i)
        if max(current) == i:
            continue
        else:
            for j in current :
                if j > i :
                    count += 1
        current.sort()
    
    answers.append((students[0], count))

for idx, ans in answers:
    print(idx, ans)