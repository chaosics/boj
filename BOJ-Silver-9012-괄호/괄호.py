import sys

# 테스트 케이스 개수 입력
t_str = sys.stdin.readline().strip()
if t_str:
    t = int(t_str)
else:
    t = 0

for _ in range(t):
    p_string = sys.stdin.readline().strip()
    stack = []
    status = True  
    
    for bracket in p_string:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack:
                status = False 
                break
            else:
                stack.pop()
        else:
            # 괄호가 아닌 다른 문자(abc 등)가 들어오면 바로 실패 처리
            status = False
            break
    
    if status and not stack:
        print("YES")
    else:
        print("NO")