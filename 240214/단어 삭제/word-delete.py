import sys
print = sys.stdout.write
tmp_str = input()
erase_str = input()
erase_len = len(erase_str)
from collections import deque

dq = deque()
idx = erase_len-1
for tmp_char in tmp_str:
    dq.append(tmp_char)
    # 끝자리가 같으면 검증 시작
    if tmp_char == erase_str[idx]:
        tmp_dq = deque()
        # idx가 넘지 않을때 끝이 동일하면 tmp_dq에 저장
        while idx != -1 and dq and dq[-1] == erase_str[idx]:
            tmp_dq.append(dq.pop())
            idx -= 1
        # 만약에 다 맞지 않으면 다시 넣어주기
        if idx != -1:
            while tmp_dq:
                dq.append(tmp_dq.pop())
        idx = erase_len-1
        
            


while dq:
    print(dq.popleft())