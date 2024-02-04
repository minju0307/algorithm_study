## 하루는 86,400초 이기 때문에 3중 for문으로 풀어도 괜찮다.

import sys
input = sys.stdin.readline

n = int(input().strip())
count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) or '3' in str(m) or '3' in str(s):
                count +=1 

print(count)