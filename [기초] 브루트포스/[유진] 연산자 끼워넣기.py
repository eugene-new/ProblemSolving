import sys

sys.stdin = open('input_files/연산자끼워넣기.txt')

n = 0
numbers = []
operators = []
visited = [False] * 12
operatorIndices = {0: '+', 1: '-', 2: '*', 3: '/'}
MAX = -1000000001
MIN = 1000000001


def calculate(a, b, operator):
    if operator == 0:
        return int(a + b)
    elif operator == 1:
        return int(a - b)
    elif operator == 2:
        return int(a * b)
    elif operator == 3:
        return int(a / b)
    else:
        return 0


def dfs(count, result):
    global MAX, MIN
    if count == n - 1:
        MAX = max(MAX, result)
        MIN = min(MIN, result)
        return

    for idx in range(0, len(operators)):
        if visited[idx] is False:
            visited[idx] = True
            new_result = calculate(result, numbers[count+1], operators[idx])
            dfs(count + 1, new_result)
            visited[idx] = False


n = int(input())
numbers = list(map(int, input().split()))
number_of_operators = list(map(int, input().split()))

for op in range(0, len(number_of_operators)):
    for _ in range(0, number_of_operators[op]):
        operators.append(op)

dfs(0, numbers[0])

print(MAX)
print(MIN)

