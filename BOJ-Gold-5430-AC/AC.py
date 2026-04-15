import sys
from collections import deque

input = sys.stdin.readline

t_line = input().strip()
if t_line:
    t = int(t_line)

    for _ in range(t):
        p = input().strip()
        n = int(input())
        s = input().strip()

        dq = deque(s[1:-1].split(',')) if n > 0 else deque()

        reverse_on = False
        error_on = False

        for fn in p:
            if fn == 'R':
                reverse_on = not reverse_on
            elif fn == 'D':
                if not dq:
                    error_on = True
                    break
                if reverse_on:
                    dq.pop()
                else:
                    dq.popleft()

        if error_on:
            print("error")
        else:
            if reverse_on:
                dq.reverse()
            print("[" + ",".join(dq) + "]")