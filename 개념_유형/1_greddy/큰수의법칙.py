import sys

n, m, k = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

numbers = sorted(numbers, reverse=True)
count = (m // k)*k

print(numbers[0]*count+numbers[1]*(m-count))
