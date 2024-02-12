import math
import sys
input = sys.stdin.readline

num = int(input().rstrip())
result = 0

def is_prime(num):
    ## 약수의 성질로 인하여 제곱근까지만 확인해도 됨
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

for n in range(num, 1000001) :
    ## 1인 경우는 소수가 아니니까 continue
    if n == 1: continue
    ## 소수이면서 팰린드롬인 수 
    ## 팰린드롬이 아니면 소수인지 확인하지 않음으로써 속도를 줄일 수 있음
    if str(n) == str(n)[::-1] and is_prime(n):
        result = n
        break

if result == 0:
    result = 1003001
    
print(result)