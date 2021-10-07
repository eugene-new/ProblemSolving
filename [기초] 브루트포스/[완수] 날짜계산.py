import sys
sys.stdin = open('input_files/날짜계산.txt')
"""
1 ≤ E ≤ 15, --> %15
1 ≤ S ≤ 28, --> %28
1 ≤ M ≤ 19. --> %19
"""

E, S, M = map(int, input().split())
# 준규 연도 설정
e, s, m = 1, 1, 1
# 우리 연도
year = 1

# e = E, s = S, m = M일때 year return
while e != E or s != S or m != M:
    # 준규 연도 + 1
    e += 1
    s += 1
    m += 1
    # 우리 연도 + 1
    year += 1
    # 범위 넘어갈때마다 1부터 다시 시작
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1

print(year)