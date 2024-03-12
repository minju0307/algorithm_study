import sys

input = sys.stdin.readline

while True:
    l1, l2, l3= map(int, input().split())
    
    if l1==l2==l3==0:
        break
    
    ## 삼각형이 가능한지 확인 
    max_num = max(l1, l2, l3)
    hap = sum(sorted([l1, l2, l3])[:2])
    if max_num >= hap :
        print("Invalid")
        continue
    
    ## 삼각형의 종류
    if l1 == l2 == l3 :
        print("Equilateral")

    elif l1 == l2 or l2 == l3 or l1 == l3:
        print("Isosceles")
    
    else:
        print("Scalene")
    
