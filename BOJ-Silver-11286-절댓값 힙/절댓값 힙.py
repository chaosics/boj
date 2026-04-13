import sys
import heapq

input = sys.stdin.readline
n = int(input().strip())
abs_heap = []

for _ in range(n):
    x = int(input().strip())
    
    if x != 0:
        heapq.heappush(abs_heap, (abs(x), x))
    else:
        if not abs_heap:
            print(0)
        else:
            print(heapq.heappop(abs_heap)[1])