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
        return a+b
    if oper_idx == 1:
        return a-b
    if oper_idx == 2:
        return a*b
    if oper_idx == 3:
        return a//b


N = int(input())
numbers = list(map(int, input().split()))
# [+, -, *, //]
operators = list(map(int, input().split()))

maximum = float('-inf')
minimum = float('inf')

dfs(0, numbers[0])
print(maximum)
print(minimum)


