import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
for r in range(n):
    for c in range(m):
        if board[r][c] == 1:
            queue.append((r, c))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while queue:
    r, c = queue.popleft()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if board[nr][nc] == 0:
                board[nr][nc] = board[r][c] + 1
                queue.append((nr, nc))

ans = 0
for row in board:
    if 0 in row:
        print(-1)
        exit()
    ans = max(ans, max(row))

print(ans - 1)