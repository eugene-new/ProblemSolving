import sys

sys.stdin = open('input_files/ABCDE.txt')

N = 0
M = 0
friend_list = [[] for _ in range(2005)]
visited = [False] * 2005
answer = 0


def dfs(current, depth):
    global answer
    if answer == 1:
        return
    elif depth == 4:
        answer = 1
        return

    for friend in friend_list[current]:
        if visited[friend] is False:
            visited[friend] = True
            dfs(friend, depth + 1)
            visited[friend] = False


N, M = map(int, input().split())


for i in range(M):
    a, b = map(int, input().split())
    friend_list[a].append(b)
    friend_list[b].append(a)

for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(answer)