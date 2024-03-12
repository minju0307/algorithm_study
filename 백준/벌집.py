import sys

input = sys.stdin.readline

n = int(input().rstrip())

for k in range(1, (1000000000//6)):
    if 1+(6*(sum(range(1,k+1)))) > n :
        break

print(k+1)