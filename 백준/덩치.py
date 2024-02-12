import sys
input = sys.stdin.readline

n = int(input().strip())
size = []

for _ in range(n):
    size.append(list(map(int, input().split())))

rank = [0] * n

for i, (x, y) in enumerate(size):
    count = 1
    for j, (p, q) in enumerate(size):
        if i == j: continue
        if x < p and y < q:
            count += 1 
    rank[i] = count

print(*rank)