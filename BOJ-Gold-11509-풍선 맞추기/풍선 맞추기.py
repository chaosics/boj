import sys

input_data = sys.stdin.read().split()

if not input_data:
    sys.exit()

n = int(input_data[0])
balloons = list(map(int, input_data[1:]))

arrows = [0] * 1000001
total_arrows = 0

for h in balloons:
    if arrows[h] > 0:
        arrows[h] -= 1
    else:
        total_arrows += 1
    
    arrows[h - 1] += 1

print(total_arrows)