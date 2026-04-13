import sys

ipv6 = sys.stdin.readline().strip()
ipv6 = ipv6.replace("::", ":empty:")
groups = ipv6.split(':')

c_groups = [g for g in groups if g != "" and g != "empty"]
missing_count = 8 - len(c_groups)

result = []
for g in groups:
    if g == 'empty':
        result.extend(['0000'] * missing_count)
    elif g != "":
        result.append(g.zfill(4))

print(":".join(result))