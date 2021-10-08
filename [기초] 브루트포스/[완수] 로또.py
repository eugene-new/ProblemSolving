# import sys
# sys.stdin = open('input_files/로또.txt')
# from itertools import combinations
#
#
# while True:
#     lst = list(map(int, input().split()))
#     k = lst[0]
#     if k == 0:
#         break
#
#     s = lst[1:]
#     numbers = []
#     for comb in combinations(s, 6):
#         numbers.append(list(comb))
#
#     for number in numbers:
#         print(*number)
#     print()


import sys
sys.stdin = open('input_files/로또.txt')


def dfs(start, ans):

    if len(ans) == 6:
        print(ans)
        return

    for i in range(start, k):
        if visited[i] == 0:
            visited[i] = 1
            ans.append(s[i])
            dfs(i+1, ans)
            ans.pop()
            visited[i] = 0


while True:
    lst = list(map(int, input().split()))
    k = lst[0]
    if k == 0:
        break

    s = lst[1:]

    visited = [0] * k
    dfs(0, [])
    print(k, s)
    print()





