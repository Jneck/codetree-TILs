import sys
input = sys.stdin.readline
n, target = input().split()
n = int(n)
for i in range(n):
    cur_str = input().strip()
    if target in cur_str:
        print(cur_str)