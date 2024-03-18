import sys
from collections import defaultdict

input = sys.stdin.readline

word = input().rstrip()
word = word.upper()
dic = defaultdict(int)
max_num = 0

for w in word:
    dic[w] += 1
    max_num = max(max_num, dic[w])

letters= []
for k, v in dic.items():
    if v == max_num:
        letters.append(k)
        

if len(letters) > 1:
    print("?")
else:
    print(letters[0])