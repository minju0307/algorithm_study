from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = defaultdict(int)
for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        dic[word] += 1

answers = sorted(list(dic.keys())) ## 3번째 조건 : 알파벳 사전 순으로 앞에 있는 단어일 수록 앞에 배치 
answers = sorted(answers, key = lambda x : len(x), reverse=True) ## 2번째 조건 : 해당 단어의 길이가 길수록 앞에 배치 
answers = sorted(answers, key=lambda x : dic[x], reverse=True) ## 1번째 조건 : 자주 나오는 단어일수록 앞에 배치

for x in answers:
    print(x)

