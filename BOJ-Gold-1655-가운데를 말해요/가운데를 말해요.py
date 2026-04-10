import sys
import heapq

input = sys.stdin.readline

def solve():
    n = int(input())
    left_heap = []  # 최대 힙
    right_heap = [] # 최소 힙

    for _ in range(n):
        pick = int(input())
        
        if len(left_heap) == len(right_heap):
            heapq.heappush(left_heap, -pick)
        else:
            heapq.heappush(right_heap, pick)
            
        if right_heap and (-left_heap[0] > right_heap[0]):
            max_val = -heapq.heappop(left_heap)
            min_val = heapq.heappop(right_heap)
            
            heapq.heappush(left_heap, -min_val)
            heapq.heappush(right_heap, max_val)
            
        print(-left_heap[0])

if __name__ == "__main__":
    solve()