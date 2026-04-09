import sys

# 분할 정복을 이용한 거듭제곱 함수
def power(a, b, c):
    # 기저 조건: 지수가 1일 때
    if b == 1:
        return a % c
    
    # 지수를 절반으로 나누어 재귀적으로 호출
    temp = power(a, b // 2, c)
    
    # 지수가 짝수인 경우: (a^(b//2))^2
    if b % 2 == 0:
        return (temp * temp) % c
    # 지수가 홀수인 경우: (a^(b//2))^2 * a
    else:
        return (temp * temp * a) % c

# 입력 처리 (A, B, C)
a, b, c = map(int, sys.stdin.readline().split())

# 결과 출력
print(power(a, b, c))
