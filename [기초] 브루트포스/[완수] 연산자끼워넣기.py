import sys
sys.stdin = open('input_files/연산자끼워넣기.txt')


def dfs(idx, tmp):
    global maximum, minimum
    if idx == N-1:
        maximum = max(tmp, maximum)
        minimum = min(tmp, minimum)
        return

    for i in range(4):
        if operators[i] == 0:
            continue
        operators[i] -= 1
        new_tmp = operation(tmp, numbers[idx+1], i)
        dfs(idx+1, new_tmp)
        operators[i] += 1


def operation(a, b, oper_idx):
    if oper_idx == 0:
        return int(a+b)
    if oper_idx == 1:
        return int(a-b)
    if oper_idx == 2:
        return int(a*b)
    if oper_idx == 3:
        return int(a/b)


N = int(input())
numbers = list(map(int, input().split()))
# [+, -, *, //]
operators = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

dfs(0, numbers[0])
print(maximum)
print(minimum)

"""
'//' 연산사 사용에 유의하자
(-1 // 5) = 0
int(-1/5) = -1
음수의 경우 0 return
"""