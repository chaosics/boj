import sys

# 1. 명령의 수 n을 입력받습니다.
n = int(sys.stdin.readline())

# 2. 데이터를 담을 바구니(스택)를 만듭니다.
stack = []

# 3. n번만큼 반복하며 명령어를 읽고 처리합니다.
for _ in range(n):
    # 공백을 기준으로 명령어를 쪼개서 리스트로 만듭니다. (예: ['push', '10'])
    command = sys.stdin.readline().split()
    
    # 4. 각 명령어에 맞는 동작을 수행합니다.
    if command[0] == "push":
        stack.append(command[1])
        
    elif command[0] == "pop":
        if not stack:  # 바구니가 비어있으면
            print(-1)
        else:
            print(stack.pop())  # 마지막 것을 삭제하며 출력
            
    elif command[0] == "size":
        print(len(stack))  # 바구니 안의 개수 출력
        
    elif command[0] == "empty":
        print(1 if not stack else 0)  # 비었으면 1, 아니면 0
        
    elif command[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])  # 마지막 것을 확인만 하고 출력