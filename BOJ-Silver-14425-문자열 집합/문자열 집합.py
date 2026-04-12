import sys

input_data = sys.stdin.read().split()

if not input_data:
    sys.exit()

n = int(input_data[0])
m = int(input_data[1])

s = set(input_data[2 : 2 + n])

count = 0
for word in input_data[2 + n : 2 + n + m]:
    if word in s:
        count += 1

print(count)