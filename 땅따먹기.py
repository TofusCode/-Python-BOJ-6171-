import sys
from fractions import Fraction

def query(x):
    global ptr
    while (ptr < len(stack)-1) and (stack[ptr + 1][2] < x):
        ptr += 1
    v = stack[ptr]
    return v[0] * x + v[1]

def insert(slope, y):
    global ptr
    point = [slope, y, -float('inf')]
    if not stack:
        stack.append(point)
        return
    while len(stack) > 1:
        top = stack[-1]
        x = intersect(top, point)
        if x <= top[2]:
            stack.pop()
        else:
            break
    point[2] = intersect(stack[-1], point)
    stack.append(point)
    if ptr >= len(stack):
        ptr = len(stack) - 1

def intersect(r, l):
    # return Fraction(l[1] - r[1], r[0] - l[0]) <= 나눗셈의 부동소수점 오차를 의심한다면 사용하자
    return (l[1] - r[1]) / (r[0] - l[0])

n = int(sys.stdin.readline())
a = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
a.sort()

p = []
ptr = 0
for i in range(n):
    while p and p[-1][1] <= a[i][1]:
        p.pop()
    p.append(a[i])

n = len(p)
dp = [0] * n
stack = []

insert(p[0][1], 0)
for i in range(n-1):
    dp[i] = query(p[i][0])
    insert(p[i+1][1], dp[i])

print(query(p[n-1][0]))