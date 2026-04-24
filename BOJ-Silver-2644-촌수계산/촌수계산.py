import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
target_x, target_y = map(int, input().split())
m = int(input())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

dist = [-1] * (n + 1)

def solve():
    q = deque([target_x])
    dist[target_x] = 0
    
    while q:
        curr = q.popleft()
        
        if curr == target_y:
            return dist[curr]
        
        for nxt in adj[curr]:
            if dist[nxt] == -1:
                dist[nxt] = dist[curr] + 1
                q.append(nxt)
    return -1

print(solve())