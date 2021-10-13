import sys

sys.stdin = open('input_files/부분수열의합.txt')


N = 0
S = 0
numbers = []

visited = [False] * 21
selected = []
answer = 0


def dfs(start, end):
    global answer
    if len(selected) == end:
        if sum(selected) == S:
            answer += 1
        return

    for i in range(start, len(numbers)):
        if visited[i] is False:
            visited[i] = True
            selected.append(numbers[i])
            dfs(i, end)
            selected.pop()
            visited[i] = False


N, S = map(int, input().split())
numbers = list(map(int, input().split()))

for count in range(1, N + 1):
    dfs(0, count)

print(answer)