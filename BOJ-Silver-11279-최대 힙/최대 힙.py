import sys
import heapq

input = sys.stdin.readline

def solve():
    n = int(input())
    max_heap = []

    for _ in range(n):
        pick = int(input())
        
        if pick == 0:     
            if not max_heap:
                print(0)
            else:
                print(-heapq.heappop(max_heap))
        else:
            heapq.heappush(max_heap, -pick)

if __name__ == "__main__":
    solve()