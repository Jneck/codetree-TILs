import sys
print = sys.stdout.write
tmp_str = input()
erase_str = input()
erase_len = len(erase_str)
idx = 0
from collections import deque

dq = deque()
for tmp_char in tmp_str:
    dq.append(tmp_char)
    if tmp_char != erase_str[idx]:
        idx = 0
        continue
    elif erase_len == idx+1:
        for i in range(erase_len):
            dq.pop()
        idx = 0
        continue
    else:
        idx += 1

while dq:
    print(dq.popleft())