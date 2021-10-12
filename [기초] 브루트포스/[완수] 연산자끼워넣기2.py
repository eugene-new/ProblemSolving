import sys
sys.stdin = open('input_files/연산자끼워넣기2.txt')


def calculate(a, b, oper_idx):
    if oper_idx == 0:
        return int(a+b)
    if oper_idx == 1:
        return int(a-b)
    if oper_idx == 2:
        return int(a*b)
    if oper_idx == 3:
        return int(a/b)


def dfs(idx, tmp):
    global maximum, minimum
    if idx == N-1:
        maximum = max(maximum, tmp)
        minimum = min(minimum, tmp)
        return

    for i in range(4):
        if operators[i] == 0:
            continue
        operators[i] -= 1
        new_tmp = calculate(tmp, numbers[idx+1], i)
        dfs(idx+1, new_tmp)
        operators[i] += 1


N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
maximum = -1e9
minimum = 1e9
dfs(0, numbers[0])
print(maximum, minimum)