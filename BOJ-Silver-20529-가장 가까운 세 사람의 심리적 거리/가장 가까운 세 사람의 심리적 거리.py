import sys
import itertools

input = sys.stdin.readline

t_line = input().strip()
if t_line:
    t = int(t_line)
    for _ in range(t):
        n = int(input())
        mbti_list = input().upper().split()
        
        if n >= 33:
            print(0)
            continue
        
        min_distance = 8
        for combo in itertools.combinations(mbti_list, 3):
            current_distance = 0
            for i in range(4):
                if not (combo[0][i] == combo[1][i] == combo[2][i]):
                    current_distance += 2
            
            min_distance = min(min_distance, current_distance)
            
            if min_distance == 0:
                break
                
        print(min_distance)