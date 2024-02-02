import sys
from collections import defaultdict

S = sys.stdin.readline().strip()
group=defaultdict(int)

if len(set(S))==1: ## 문자열이 같은 것들로만 이루어진 경우 
    print(0) 
else:
    for idx, s in enumerate(S):
        if idx == 0 : 
            group[s]+=1
            continue
        if S[idx-1] != s:
            group[s]+=1

    print(min(group.values()))   