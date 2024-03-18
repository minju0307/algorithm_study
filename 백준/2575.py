import sys
input = sys.stdin.readline

game = {"Y":2, "F":3, "O":4}
n, type = input().split()
people=[]

for _ in range(int(n)):
    people.append(input().rstrip())
    
new_members=len(list(set(people)))

print(new_members//(game[type]-1))