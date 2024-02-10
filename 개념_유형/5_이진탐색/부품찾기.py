import sys
input = sys.stdin.readline

n = int(input().rstrip())
items = list(map(int, input().rstrip().split()))
check = [0] * (max(items)+1)
for i in items:
    check[i] += 1 
    
m = int(input().rstrip())
query = list(map(int, input().rstrip().split()))

for q in query:
    if check[q] >= 1:
        print('yes')
    else:
        print('no')