import sys

S = sys.stdin.readline().strip()
n = len(S)
s = set()

for i in range(n):
    for j in range(i + 1, n + 1):
        s.add(S[i:j])

print(len(s))