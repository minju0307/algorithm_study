import sys
import math 

input = sys.stdin.readline

h, w, n, m = map(int, input().split())

print(math.ceil(h/(1+n)) * math.ceil(w/(1+m)))
