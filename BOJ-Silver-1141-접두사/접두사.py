import sys

input = sys.stdin.readline
n = int(input().strip())
words = []

for _ in range(n):
    words.append(input().strip())

words.sort()

ans = n
for i in range(n - 1):
    if words[i+1].startswith(words[i]):
        ans -= 1

print(ans)