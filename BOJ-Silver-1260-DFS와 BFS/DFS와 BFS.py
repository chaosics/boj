import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

for i in range(1, n + 1):
    adj[i].sort()

visited_dfs = [False] * (n + 1)
def dfs(now):
    visited_dfs[now] = True
    print(now, end=' ')
    for neighbor in adj[now]:
        if not visited_dfs[neighbor]:
            dfs(neighbor)

visited_bfs = [False] * (n + 1)
def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for neighbor in adj[now]:
            if not visited_bfs[neighbor]:
                visited_bfs[neighbor] = True
                queue.append(neighbor)

dfs(v)
print()
bfs(v)
print()